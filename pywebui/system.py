from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class SysInfo(ResponseObject): pass


class ResInfo(ResponseObject): pass


class SystemMethods:
    def get_sysinfo(self):
        r = self.get(urls.API_GET_SYSTEM_INFO)

        if r.status_code == 200:
            return SysInfo(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_resinfo(self):
        r = self.get(urls.API_GET_SYSTEM_RESOURCES)

        if r.status_code == 200:
            return ResInfo(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])
