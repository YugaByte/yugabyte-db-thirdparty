# Copyright (c) Yugabyte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

import os

from yugabyte_db_thirdparty.util import YB_THIRDPARTY_DIR


CHECKSUM_FILE_NAME = 'thirdparty_src_checksums.txt'
CHECKSUM_SUFFIX = '.sha256'


def get_checksum_file_path() -> str:
    return os.path.join(YB_THIRDPARTY_DIR, CHECKSUM_FILE_NAME)
