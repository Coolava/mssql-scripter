# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import logging
import logging.config
import os


def get_config_log_file():
    # TODO: Refine this
    log_dir = os.path.join(
        os.path.expanduser(
            os.path.join(
                '~', '.mssql.scripter')))
    if (not os.path.exists(log_dir)):
        os.makedirs(log_dir)

    return os.path.join(log_dir, 'mssql-scripter.log')


logging.basicConfig(
    filename=get_config_log_file(),
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)
