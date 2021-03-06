#   Copyright 2012 OpenStack Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import pbr.version

from novaclient import api_versions


__version__ = pbr.version.VersionInfo('python-novaclient').version_string()

API_MIN_VERSION = api_versions.APIVersion("2.1")
# The max version should be the latest version that is supported in the client,
# not necessarily the latest that the server can provide. This is what a user
# can opt into with the --os-compute-api-version option on the CLI. Note that
# there may be gaps in supported microversions before this max version which is
# why novaclient.shell.DEFAULT_OS_COMPUTE_API_VERSION is not 2.latest or
# necessarily equal to API_MAX_VERSION.
API_MAX_VERSION = api_versions.APIVersion("2.11")
