# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module contains the implementation of an autonomous economic agent (AEA)."""
import datetime
import logging
from asyncio import AbstractEventLoop
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    cast,
)

from aea.agent import Agent
from aea.agent_loop import AsyncAgentLoop, BaseAgentLoop
from aea.configurations.base import PublicId
from aea.configurations.constants import DEFAULT_SKILL
from aea.connections.base import Connection
from aea.context.base import AgentContext
from aea.crypto.wallet import Wallet
from aea.decision_maker.base import DecisionMakerHandler
from aea.decision_maker.default import (
    DecisionMakerHandler as DefaultDecisionMakerHandler,
)
from aea.exceptions import AEAException
from aea.helpers.exception_policy import ExceptionPolicyEnum
from aea.helpers.exec_timeout import ExecTimeoutThreadGuard, TimeoutException
from aea.helpers.logging import AgentLoggerAdapter, WithLogger
from aea.identity.base import Identity
from aea.mail.base import Envelope
from aea.protocols.base import Message
from aea.protocols.default.message import DefaultMessage
from aea.registries.filter import Filter
from aea.registries.resources import Resources
from aea.skills.base import Behaviour, Handler
from aea.skills.error.handlers import ErrorHandler


class AEA(Agent, WithLogger):
    """This class implements an autonomous economic agent."""

    RUN_LOOPS: Dict[str, Type[BaseAgentLoop]] = {
        "async": AsyncAgentLoop,
    }
    DEFAULT_RUN_LOOP: str = "async"

    def __init__(
        self,
        identity: Identity,
        wallet: Wallet,
        resources: Resources,
        loop: Optional[AbstractEventLoop] = None,
        period: float = 0.05,
        execution_timeout: float = 0,
        max_reactions: int = 20,
        decision_maker_handler_class: Type[
            DecisionMakerHandler
        ] = DefaultDecisionMakerHandler,
        skill_exception_policy: ExceptionPolicyEnum = ExceptionPolicyEnum.propagate,
        loop_mode: Optional[str] = None,
        runtime_mode: Optional[str] = None,
        default_connection: Optional[PublicId] = None,
        default_routing: Optional[Dict[PublicId, PublicId]] = None,
        connection_ids: Optional[Collection[PublicId]] = None,
        search_service_address: str = "fetchai/soef:*",
        **kwargs,
    ) -> None:
        """
        Instantiate the agent.

        :param identity: the identity of the agent
        :param wallet: the wallet of the agent.
        :param resources: the resources (protocols and skills) of the agent.
        :param loop: the event loop to run the connections.
        :param period: period to call agent's act
        :param exeution_timeout: amount of time to limit single act/handle to execute.
        :param max_reactions: the processing rate of envelopes per tick (i.e. single loop).
        :param decision_maker_handler_class: the class implementing the decision maker handler to be used.
        :param skill_exception_policy: the skill exception policy enum
        :param loop_mode: loop_mode to choose agent run loop.
        :param runtime_mode: runtime mode (async, threaded) to run AEA in.
        :param default_connection: public id to the default connection
        :param default_routing: dictionary for default routing.
        :param connection_ids: active connection ids. Default: consider all the ones in the resources.
        :param search_service_address: the address of the search service used.
        :param kwargs: keyword arguments to be attached in the agent context namespace.

        :return: None
        """
        super().__init__(
            identity=identity,
            connections=[],
            loop=loop,
            period=period,
            loop_mode=loop_mode,
            runtime_mode=runtime_mode,
        )
        aea_logger = AgentLoggerAdapter(
            logger=logging.getLogger(__name__), agent_name=identity.name
        )
        WithLogger.__init__(self, logger=cast(logging.Logger, aea_logger))

        self.max_reactions = max_reactions
        decision_maker_handler = decision_maker_handler_class(
            identity=identity, wallet=wallet
        )
        self.runtime.set_decision_maker(decision_maker_handler)

        self._context = AgentContext(
            self.identity,
            self.runtime.multiplexer.connection_status,
            self.outbox,
            self.runtime.decision_maker.message_in_queue,
            decision_maker_handler.context,
            self.runtime.task_manager,
            default_connection,
            default_routing if default_routing is not None else {},
            search_service_address,
            **kwargs,
        )
        self._execution_timeout = execution_timeout
        self._connection_ids = connection_ids
        self._resources = resources
        self._filter = Filter(
            self.resources, self.runtime.decision_maker.message_out_queue
        )

        self._skills_exception_policy = skill_exception_policy

        self._setup_loggers()

    @property
    def context(self) -> AgentContext:
        """Get (agent) context."""
        return self._context

    @property
    def resources(self) -> Resources:
        """Get resources."""
        return self._resources

    @resources.setter
    def resources(self, resources: "Resources") -> None:
        """Set resources."""
        self._resources = resources

    @property
    def filter(self) -> Filter:
        """Get the filter."""
        return self._filter

    @property
    def active_behaviours(self) -> List[Behaviour]:
        """Get all active behaviours to use in act."""
        return self.filter.get_active_behaviours()

    def setup(self) -> None:
        """
        Set up the agent.

        Performs the following:

        - loads the resources (unless in programmatic mode)
        - calls setup() on the resources

        :return: None
        """
        self.resources.setup()
        ExecTimeoutThreadGuard.start()

    def act(self) -> None:
        """
        Perform actions.

        Calls act() of each active behaviour.

        :return: None
        """
        self.filter.handle_new_handlers_and_behaviours()

    @property
    def active_connections(self) -> List[Connection]:
        """Return list of active connections."""
        connections = self.resources.get_all_connections()
        if self._connection_ids is not None:
            connections = [
                c for c in connections if c.connection_id in self._connection_ids
            ]
        return connections

    def _get_multiplexer_setup_options(self) -> Optional[Dict]:
        return dict(
            connections=self.active_connections,
            default_routing=self.context.default_routing,
            default_connection=self.context.default_connection,
        )

    def _get_error_handler(self) -> Optional[Handler]:
        """Get error handler."""
        return self.resources.get_handler(DefaultMessage.protocol_id, DEFAULT_SKILL)

    def _get_msg_and_handlers_for_envelope(
        self, envelope: Envelope
    ) -> Tuple[Optional[Message], List[Handler]]:
        protocol = self.resources.get_protocol(envelope.protocol_id)

        # TODO specify error handler in config and make this work for different skill/protocol versions.
        error_handler = self._get_error_handler()

        if error_handler is None:
            self.logger.warning("ErrorHandler not initialized. Stopping AEA!")
            self.stop()
            return None, []
        error_handler = cast(ErrorHandler, error_handler)

        if protocol is None:
            error_handler.send_unsupported_protocol(envelope)
            return None, []

        if isinstance(envelope.message, Message):
            msg = envelope.message
        else:
            try:
                msg = protocol.serializer.decode(envelope.message)
                msg.sender = envelope.sender
                msg.to = envelope.to
            except Exception as e:  # pylint: disable=broad-except  # thats ok, because we send the decoding error back
                self.logger.warning("Decoding error. Exception: {}".format(str(e)))
                error_handler.send_decoding_error(envelope)
                return None, []

        handlers = self.filter.get_active_handlers(
            protocol.public_id, envelope.skill_id
        )

        if len(handlers) == 0:
            error_handler.send_unsupported_skill(envelope)
            return None, []

        return msg, handlers

    def handle_envelope(self, envelope: Envelope) -> None:
        """
        Handle an envelope.

        :param envelope: the envelope to handle.
        :return: None
        """
        self.logger.debug("Handling envelope: {}".format(envelope))
        msg, handlers = self._get_msg_and_handlers_for_envelope(envelope)

        if msg is None:
            return

        for handler in handlers:
            self._handle_message_with_handler(msg, handler)

    def _handle_message_with_handler(self, message: Message, handler: Handler) -> None:
        """
        Handle one message with one predefined handler.

        :param message: message to be handled.
        :param handler: handler suitable for this message protocol.
        """
        self._execution_control(handler.handle, [message])

    def _execution_control(
        self,
        fn: Callable,
        args: Optional[Sequence] = None,
        kwargs: Optional[Dict] = None,
    ) -> Any:
        """
        Execute skill function in exception handling environment.

        Logs error, stop agent or propagate excepion depends on policy defined.

        :param fn: function to call
        :param args: optional sequence of arguments to pass to function on call
        :param kwargs: optional dict of keyword arguments to pass to function on call

        :return: same as function
        """
        # docstyle: ignore # noqa: E800
        def log_exception(e, fn):
            self.logger.exception(f"<{e}> raised during `{fn}`")

        try:
            with ExecTimeoutThreadGuard(self._execution_timeout):
                return fn(*(args or []), **(kwargs or {}))
        except TimeoutException:
            self.logger.warning(
                "`{}` was terminated as its execution exceeded the timeout of {} seconds. Please refactor your code!".format(
                    fn, self._execution_timeout
                )
            )
        except Exception as e:  # pylint: disable=broad-except
            if self._skills_exception_policy == ExceptionPolicyEnum.propagate:
                raise
            if self._skills_exception_policy == ExceptionPolicyEnum.stop_and_exit:
                log_exception(e, fn)
                self.stop()
                raise AEAException(
                    f"AEA was terminated cause exception `{e}` in skills {fn}! Please check logs."
                )
            if self._skills_exception_policy == ExceptionPolicyEnum.just_log:
                log_exception(e, fn)
            else:
                raise AEAException(
                    f"Unsupported exception policy: {self._skills_exception_policy}"
                )

    def teardown(self) -> None:
        """
        Tear down the agent.

        Performs the following:

        - tears down the resources.

        :return: None
        """
        self.logger.debug("[{}]: Calling teardown method...".format(self.name))
        self.resources.teardown()
        ExecTimeoutThreadGuard.stop()

    def _setup_loggers(self):
        """Set up logger with agent name."""
        for element in [
            self.runtime.main_loop,
            self.runtime.multiplexer,
            self.runtime.task_manager,
            self.resources.component_registry,
            self.resources.behaviour_registry,
            self.resources.handler_registry,
            self.resources.model_registry,
        ]:
            element.logger = AgentLoggerAdapter(
                element.logger, agent_name=self._identity.name
            )

    def get_periodic_tasks(
        self,
    ) -> Dict[Callable, Tuple[float, Optional[datetime.datetime]]]:
        """
        Get all periodic tasks for agent.

        :return: dict of callable with period specified
        """
        tasks = super().get_periodic_tasks()
        tasks.update(self._get_behaviours_tasks())
        return tasks

    def _get_behaviours_tasks(
        self,
    ) -> Dict[Callable, Tuple[float, Optional[datetime.datetime]]]:
        """
        Get all periodic tasks for AEA behaviours.

        :return: dict of callable with period specified
        """
        tasks = {}

        for behaviour in self.active_behaviours:
            tasks[behaviour.act_wrapper] = (behaviour.tick_interval, behaviour.start_at)

        return tasks

    def get_message_handlers(self) -> List[Tuple[Callable[[Any], None], Callable]]:
        """
        Get handlers with message getters.

        :return: List of tuples of callables: handler and coroutine to get a message
        """
        return super(AEA, self).get_message_handlers() + [
            (self.filter.handle_internal_message, self.filter.get_internal_message,),
        ]
