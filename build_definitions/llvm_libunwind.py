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
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build_definitions import *  # noqa


class LlvmLibUnwindDependency(Dependency):
    def __init__(self) -> None:
        super(LlvmLibUnwindDependency, self).__init__(
            name='llvm_libunwind',
            version='10.0.1',
            url_pattern='https://github.com/llvm/llvm-project/releases/tag/llvmorg-{}',
            build_group=BUILD_GROUP_COMMON)

    def build(self, builder: BuilderInterface) -> None:
        builder.build_with_cmake(
            self,
            extra_args=[
                '-DCMAKE_BUILD_TYPE=Release',
                '-DLLVM_ENABLE_PROJECTS=libunwind',
                '-DBUILD_SHARED_LIBS=ON',
                '-DLIBUNWIND_USE_COMPILER_RT=ON'
            ])
