from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class SystemParameter(ResponseObject):
    def __repr__(self):
        return f'{self.name}={self.currentValue}'


class SystemParametersMethods:
    def get_current_parameters(self, group):
        parameters = []
        r = self.get(urls.API_GET_CURRENT_SYSGEN, group=group)
        if r.status_code == 200:
            for attrs in r.json():
                parameters.append(SystemParameter(attrs))

        return parameters

    def get_active_parameters(self, group):
        parameters = []
        r = self.get(urls.API_GET_ACTIVE_SYSGEN, group=group)
        if r.status_code == 200:
            for attrs in r.json():
                parameters.append(SystemParameter(attrs))

        return parameters

    def edit_parameter(self, source, parameter, value):
        data = [
            {
                "dataSource": source,
                "paramName": parameter,
                "paramValue": str(value)
            }
        ]

        r = self.put(urls.API_EDIT_SYSGEN, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
