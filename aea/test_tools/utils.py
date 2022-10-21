# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2022 Valory AG
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

"""Helpful utilities."""

import os
import shutil
import time
from pathlib import Path
from typing import Callable, Union


def wait_for_condition(
    condition_checker: Callable,
    timeout: int = 2,
    error_msg: str = "Timeout",
    period: float = 0.001,
) -> None:
    """Wait for condition to occur in selected timeout."""

    start_time = time.time()
    while not condition_checker():
        time.sleep(period)
        if time.time() > start_time + timeout:
            raise TimeoutError(error_msg)


def remove_test_directory(directory: Union[str, Path], retries: int = 3) -> bool:
    """Destroy a directory once tests are done, change permissions if needed.

    Note that on Windows directories and files that are open cannot be deleted.

    :param directory: directory to be deleted
    :param retries: number of re-attempts
    :return: whether the directory was successfully deleted
    """

    while os.path.exists(directory) and retries:
        try:
            os.chmod(directory, 0o777)  # nosec
            shutil.rmtree(directory)
        except Exception:  # pylint: disable=broad-except
            retries -= 1
            time.sleep(1)
    return not os.path.exists(directory)
