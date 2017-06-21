#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

from fabric.api import *
from fabric.contrib import files

from lib import helpers

@task
def enable():
    files.upload_template(
        os.path.join(
            helpers.__fabric_lib_dir, 'templates', 'dm_snapshot.conf'
        ),
        '/etc/modules-load.d/dm_snapshot.conf',
        use_sudo=True,
        backup=False,
    )
    sudo(
        "modprobe dm_snapshot && modprobe dm_mirror && modprobe dm_thin_pool"
    )