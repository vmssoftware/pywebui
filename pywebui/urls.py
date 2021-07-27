# Module contains urls of API endpoints

API_LOGIN = '/login'
API_GET_VERSION = '/api/version'

API_GET_PROCESS_LIST = '/api/processes'
API_GET_PROCESS_DETAIL = '/api/processes/{pid}'
API_KILL_PROCESS = '/api/processes/{pid}/kill'
API_EDIT_PROCESS = '/api/processes/{pid}/edit'
API_SUSPEND_PROCESS = '/api/processes/{pid}/suspend'
API_RESUME_PROCESS = '/api/processes/{pid}/resume'

API_GET_USER_LIST = '/api/users'
API_GET_USER_DETAIL = '/api/users/{username}'
API_ADD_USER = '/api/users'
API_EDIT_USER = '/api/users/{username}'
API_DELETE_USER = '/api/users/{username}'
API_DUPLICATE_USER = '/api/users/{username}/duplicate'
API_ENABLE_USER = '/api/users/{username}/enable'
API_DISABLE_USER = '/api/users/{username}/disable'

API_GET_SYSTEM_INFO = '/api/getsyi'
API_GET_SYSTEM_RESOURCES = '/api/getrmi'

API_GET_ALL_LICENSES_LIST = '/api/licenses'
API_GET_ACTIVE_LICENSES_LIST = '/api/licenses?active'
API_GET_LICENSE = '/api/licenses/{product}/{authorization}'
API_GET_LICENSE_HISTORY = '/api/licenses/{product}/{authorization}/history'
API_DELETE_LICENSE_HISTORY = '/api/licenses/{product}/{authorization}/history'
API_EXPORT_LICENSE_HISTORY = '/api/licenses/{product}/{authorization}/history/export'
API_ENABLE_LICENSE = '/api/licenses/{product}/{authorization}/enable'
API_DISABLE_LICENSE = '/api/licenses/{product}/{authorization}/disable'
API_DELETE_LICENSE = '/api/licenses/{product}/{authorization}'
API_LOAD_LICENSE = '/api/licenses/{product}/{authorization}/load'
API_UNLOAD_LICENSE = '/api/licenses/{product}/unload'
API_REGISTER_LICENSE = '/api/licenses/{product}/register'

API_GET_DISKS = '/api/disks'
API_GET_DISK_DETAIL = '/api/disks/{device}'

API_GET_REPORTS = '/api/reports'
API_GET_REPORT = '/api/reports/{filename}?fileDir={directory}'
API_EXPORT_REPORT = '/api/reports/{filename}/export?fileDir={directory}'
API_GET_REPORT_LOG = '/api/reports/{filename}/export?fileDir={directory}'
API_GENERATE_REPORTS = '/api/reports'

API_GET_INSTALLED_PACKAGES = '/api/pcsi'
API_GET_INSTALLED_PACKAGE_HISTORY = '/api/pcsi/{product}'
API_EXPORT_INSTALLED_PACKAGE_HISTORY = '/api/pcsi/{product}/export'
API_DELETE_INSTALLED_PACKAGE = '/api/pcsi/{product}'

API_GET_CURRENT_SYSGEN = '/api/sysgen/?dataSource=current&group={group}'
API_GET_ACTIVE_SYSGEN = '/api/sysgen/?dataSource=active&group={group}'
API_EDIT_SYSGEN = '/api/sysgen'

API_GET_IDENTIFIERS = '/api/identifiers?0'
API_GET_ALL_IDENTIFIERS = '/api/identifiers'
API_GET_IDENTIFIER_HOLDERS = '/api/identifiers/{identifier}'
API_GET_HOLDER_IDENTIFIERS = '/api/holders/{holder}'
API_CREATE_IDENTIFIER = '/api/identifiers'
API_REVOKE_IDENTIFIERS = '/api/identifiers/revoke'
API_GRANT_IDENTIFIERS = '/api/identifiers/grant'
API_DELETE_IDENTIFIER = '/api/identifiers/{identifier}'

API_GET_BATCH_QUEUES = '/api/queues?batch'
API_GET_PRINTER_QUEUES = '/api/queues?printer'
API_GET_QUEUE_DETAIL = '/api/queues/{queue}'
API_START_QUEUE = '/api/queues/{queue}/start'
API_PAUSE_QUEUE = '/api/queues/{queue}/pause'
API_STOP_QUEUE = '/api/queues/{queue}/stop'
API_EDIT_QUEUE_DESCRIPTION = '/api/queues/{queue}/edit'
API_START_JOB = '/api/jobs/{job}/start'
API_PAUSE_JOB = '/api/jobs/{job}/pause'
API_DELETE_JOB = '/api/jobs/{job}/delete'

API_GET_NODES = '/api/nodes'

API_GET_ALERTS = '/api/alerts'
API_GET_BOOKMARKS = '/api/bookmarks'
API_ADD_BOOKMARK = '/api/bookmarks'
API_DELETE_BOOKMARK = '/api/bookmarks'

API_GET_DEVICES = '/api/tcpip/devices'
API_GET_DEVICE = '/api/tcpip/devices/{name}'

API_GET_HOSTS = '/api/tcpip/hosts'
API_ADD_HOST = '/api/tcpip/hosts'
API_EDIT_HOST = '/api/tcpip/hosts/{name}/{address}'
API_DELETE_HOST = '/api/tcpip/hosts/{name}/{address}'

API_GET_INTERFACES = '/api/tcpip/interfaces'
API_GET_INTERFACE = '/api/tcpip/interfaces/{name}'

API_GET_NETSTAT = '/api/tcpip/netstat'

API_GET_SERVICES = '/api/tcpip/services'
API_ADD_SERVICE = '/api/tcpip/services'
API_EDIT_SERVICE = '/api/tcpip/services/{name}'
API_DELETE_SERVICE = '/api/tcpip/services/{name}'

API_GET_SUBSYSTEMS = '/api/tcpip/sysconfig'
API_GET_SUBSYSTEM = '/api/tcpip/sysconfig/{name}'
API_EDIT_SUBSYSTEMS = '/api/tcpip/sysconfig/{name}'
