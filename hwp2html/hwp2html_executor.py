# Copyright 2019 Na Kyung Hyun

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import subprocess

from pkg_resources import resource_filename

HWP2HTML_COMMAND = "java -jar %s %s %s"

class Hwp2HtmlExecutor(object):
    def execute(self, fileName, path):

        here = os.path.dirname(__file__)
        
        command = HWP2HTML_COMMAND % (os.path.join(here, 'java', 'hwplib-1.0.0.jar'), fileName, path)

        output = subprocess.check_call(
            command,    
            stderr = subprocess.STDOUT,
            shell  = True
        )

        print(output)

        return output#.decoding('utf-8')