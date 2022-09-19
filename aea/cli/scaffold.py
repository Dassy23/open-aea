# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
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
"""Implementation of the 'aea scaffold' subcommand."""
import logging
import os
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import cast

import click
from jsonschema import ValidationError

from aea import AEA_DIR
from aea.cli.fingerprint import fingerprint_item
from aea.cli.utils.context import Context
from aea.cli.utils.decorators import check_aea_project, clean_after, pass_ctx
from aea.cli.utils.loggers import logger
from aea.cli.utils.package_utils import (
    create_symlink_packages_to_vendor,
    create_symlink_vendor_to_local,
    validate_package_name,
)
from aea.configurations.base import PublicId
from aea.configurations.constants import (  # noqa: F401  # pylint: disable=unused-import
    CONNECTION,
    CONTRACT,
    DEFAULT_AEA_CONFIG_FILE,
    DEFAULT_CONNECTION_CONFIG_FILE,
    DEFAULT_CONTRACT_CONFIG_FILE,
    DEFAULT_PROTOCOL_CONFIG_FILE,
    DEFAULT_SKILL_CONFIG_FILE,
    DEFAULT_VERSION,
    DOTTED_PATH_MODULE_ELEMENT_SEPARATOR,
    PROTOCOL,
    SCAFFOLD_PUBLIC_ID,
    SKILL,
)
from aea.helpers.io import open_file
from aea.helpers.ipfs.base import IPFSHashOnly


COPYRIGHT_HEADER_TEMPLATE = """\
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright {year} Valory AG
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
"""


def update_copyright_headers(path: Path) -> None:
    """Update copyright headers"""

    # this allows for arbitrary authors
    year = datetime.now().year
    top = "\n".join(COPYRIGHT_HEADER_TEMPLATE.split("\n")[:3])
    bottom = "\n".join(COPYRIGHT_HEADER_TEMPLATE.split("\n")[-15:])
    new_copyright_header = COPYRIGHT_HEADER_TEMPLATE.format(year=year)

    for file in path.rglob("**/*.py"):
        content = file.read_text()
        i, j = content.find(top), content.find(bottom)
        if i == j == -1:  # no copyright header present yet
            file.write_text(f"{new_copyright_header}\n{content}")
        elif i != j != -1:  # copyright header detected
            old_copyright_header = content[i : j + len(bottom)]
            content = content.replace(old_copyright_header, new_copyright_header)
            file.write_text(content)
        else:
            raise ValueError(f"Copyright pattern detection failed: {content}")


@click.group()
@click.option(
    "--to-local-registry",
    "-tlr",
    is_flag=True,
    help="Scaffold skill inside a local registry.",
)
@click.option(
    "--with-symlinks",
    is_flag=True,
    help="Add symlinks from vendor to non-vendor and packages to vendor folders.",
)
@click.pass_context
@check_aea_project
def scaffold(
    click_context: click.core.Context,
    with_symlinks: bool,
    to_local_registry: bool,
) -> None:  # pylint: disable=unused-argument
    """Scaffold a package for the agent."""
    ctx = cast(Context, click_context.obj)
    ctx.set_config("with_symlinks", with_symlinks)
    ctx.set_config("to_local_registry", to_local_registry)


@scaffold.command()
@click.argument("connection_name", type=str, required=True)
@pass_ctx
def connection(ctx: Context, connection_name: str) -> None:
    """Add a connection scaffolding to the configuration file and agent."""
    scaffold_item(ctx, CONNECTION, connection_name)


@scaffold.command()
@click.argument("contract_name", type=str, required=True)
@pass_ctx
def contract(ctx: Context, contract_name: str) -> None:
    """Add a contract scaffolding to the configuration file and agent."""
    scaffold_item(ctx, CONTRACT, contract_name)


@scaffold.command()
@click.argument("protocol_name", type=str, required=True)
@click.option("-y", "--yes", is_flag=True, default=False)
@pass_ctx
def protocol(ctx: Context, protocol_name: str, yes: bool) -> None:
    """Add a protocol scaffolding to the configuration file and agent."""
    if yes or click.confirm(
        "We highly recommend auto-generating protocols with the aea generate command. Do you really want to continue scaffolding?"
    ):
        scaffold_item(ctx, PROTOCOL, protocol_name)
    else:
        click.echo("Aborted. Exit")  # pragma: nocover


@scaffold.command()
@click.argument("skill_name", type=str, required=True)
@pass_ctx
def skill(ctx: Context, skill_name: str) -> None:
    """Add a skill scaffolding to the configuration file and agent."""
    scaffold_item(ctx, SKILL, skill_name)


@scaffold.command()
@pass_ctx
def decision_maker_handler(ctx: Context) -> None:
    """Add a decision maker scaffolding to the configuration file and agent."""
    _scaffold_dm_handler(ctx)


@scaffold.command()
@pass_ctx
def error_handler(ctx: Context) -> None:
    """Add an error scaffolding to the configuration file and agent."""
    _scaffold_error_handler(ctx)


@clean_after
def scaffold_item(ctx: Context, item_type: str, item_name: str) -> None:
    """
    Add an item scaffolding to the configuration file and agent.

    :param ctx: Context object.
    :param item_type: type of item.
    :param item_name: item name.

    :raises ClickException: if some error occurs.
    """
    validate_package_name(item_name)
    author_name = ctx.agent_config.author
    loader = getattr(ctx, f"{item_type}_loader")
    default_config_filename = globals()[f"DEFAULT_{item_type.upper()}_CONFIG_FILE"]

    to_local_registry = ctx.config.get("to_local_registry")

    item_type_plural = item_type + "s"
    existing_ids = getattr(ctx.agent_config, f"{item_type}s")
    existing_ids_only_author_and_name = map(lambda x: (x.author, x.name), existing_ids)
    # check if we already have an item with the same public id
    if (author_name, item_name) in existing_ids_only_author_and_name:
        raise click.ClickException(
            f"A {item_type} with name '{item_name}' already exists. Aborting..."
        )

    agent_name = ctx.agent_config.agent_name

    # create the item folder
    if to_local_registry:
        click.echo(f"Adding {item_type} scaffold '{item_name}' to local registry...")
        dest = Path(str(ctx.agent_config.directory)) / Path(item_type_plural)
    else:
        click.echo(
            f"Adding {item_type} scaffold '{item_name}' to the agent '{agent_name}'..."
        )
        dest = Path(item_type_plural)

    dest.mkdir(exist_ok=True)
    dest = dest / item_name

    if os.path.exists(dest):
        raise click.ClickException(
            f"A {item_type} with this name already exists. Please choose a different name and try again."
        )

    ctx.clean_paths.append(str(dest))
    try:
        # copy the item package into the agent project.
        src = Path(os.path.join(AEA_DIR, item_type_plural, "scaffold"))
        logger.debug(f"Copying {item_type} modules. src={src} dst={dest}")
        shutil.copytree(src, dest)
        update_copyright_headers(dest)

        new_public_id = PublicId(author_name, item_name, DEFAULT_VERSION)

        # ensure the name in the yaml and the name of the folder are the same
        if to_local_registry:
            config_filepath = dest / default_config_filename
        else:
            config_filepath = Path(
                ctx.cwd, item_type_plural, item_name, default_config_filename
            )

        with open_file(config_filepath) as fp:
            config = loader.load(fp)
        config.name = item_name
        config.author = author_name
        with open_file(config_filepath, "w") as fp:
            loader.dump(config, fp)

        # update 'PUBLIC_ID' variable with the right public id in connection.py!

        for file_name in ["__init__.py", "connection.py"]:
            file_path = Path(dest) / file_name
            if not file_path.exists():
                continue
            py_file = Path(file_path)
            py_file.write_text(
                re.sub(SCAFFOLD_PUBLIC_ID, str(new_public_id), py_file.read_text())
            )

        # fingerprint item.
        if to_local_registry:
            ctx.cwd = str(ctx.agent_config.directory)
            fingerprint_item(ctx, item_type, new_public_id)
        else:
            fingerprint_item(ctx, item_type, new_public_id)

        package_hash = IPFSHashOnly().hash_directory(str(dest))
        new_public_id_with_hash = PublicId(
            author_name, item_name, DEFAULT_VERSION, package_hash
        )
        if not to_local_registry:
            logger.debug(f"Registering the {item_type} into {DEFAULT_AEA_CONFIG_FILE}")
            existing_ids.add(new_public_id_with_hash)
            with open_file(os.path.join(ctx.cwd, DEFAULT_AEA_CONFIG_FILE), "w") as fp:
                ctx.agent_loader.dump(ctx.agent_config, fp)

        if ctx.config.get("with_symlinks", False):
            click.echo(
                "Adding symlinks from vendor to non-vendor and packages to vendor folders."
            )
            create_symlink_vendor_to_local(ctx, item_type, new_public_id)
            create_symlink_packages_to_vendor(ctx)

    except ValidationError:
        raise click.ClickException(
            f"Error when validating the {item_type} configuration file."
        )
    except Exception as e:
        raise click.ClickException(str(e))


def _scaffold_dm_handler(ctx: Context) -> None:
    """Scaffold the decision maker handler."""
    _scaffold_non_package_item(
        ctx,
        "decision_maker_handler",
        "decision maker handler",
        "DecisionMakerHandler",
        "decision_maker",
    )


def _scaffold_error_handler(ctx: Context) -> None:
    """Scaffold the error handler."""
    _scaffold_non_package_item(
        ctx, "error_handler", "error handler", "ErrorHandler", "error_handler"
    )


def _scaffold_non_package_item(
    ctx: Context, item_type: str, type_name: str, class_name: str, aea_dir: str
) -> None:
    """
    Scaffold a non-package item (e.g. decision maker handler, or error handler).

    :param ctx: the CLI context.
    :param item_type: the item type (e.g. 'decision_maker_handler')
    :param type_name: the type name (e.g. "decision maker")
    :param class_name: the class name (e.g. "DecisionMakerHandler")
    :param aea_dir: the AEA directory that contains the scaffold module
    """
    existing_item = getattr(ctx.agent_config, item_type)
    if existing_item != {}:
        raise click.ClickException(
            f"A {type_name} specification already exists. Aborting..."
        )

    dest = Path(f"{item_type}.py")
    agent_name = ctx.agent_config.agent_name
    click.echo(f"Adding {type_name} scaffold to the agent '{agent_name}'...")
    # create the file name
    dotted_path = f".{item_type}{DOTTED_PATH_MODULE_ELEMENT_SEPARATOR}{class_name}"
    try:
        # copy the item package into the agent project.
        src = Path(os.path.join(AEA_DIR, aea_dir, "scaffold.py"))
        logger.debug(f"Copying {type_name}. src={src} dst={dest}")
        shutil.copyfile(src, dest)

        # add the item to the configurations.
        logger.debug(f"Registering the {type_name} into {DEFAULT_AEA_CONFIG_FILE}")
        setattr(
            ctx.agent_config,
            item_type,
            {
                "dotted_path": str(dotted_path),
                "file_path": str(os.path.join(".", dest)),
                "config": {},
            },
        )
        ctx.agent_loader.dump(
            ctx.agent_config,
            open_file(os.path.join(ctx.cwd, DEFAULT_AEA_CONFIG_FILE), "w"),
        )

    except Exception as e:
        os.remove(dest)
        raise click.ClickException(str(e))
