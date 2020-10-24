from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class SystemParameter(ResponseObject):
    """SystemParameter object.

    Attributes:
        currentValue (str): The current value of system parameter.
        defaultValue (str): The default value of system parameter.
        dynamic	(bool): The parameter attribute which means that value can be modified (true or false).
        maxValue (str): The maximum value of system parameter.
        minValue (str): The minimum value of system parameter.
        name (str): The name of system parameter.
        unit (str): The unit of system parameter.
    """
    def __repr__(self):
        return f'{self.name}={self.currentValue}'


class SystemParametersMethods:
    """Encapsulates methods for manage system parameters."""

    def get_current_parameters(self, group: str) -> List[SystemParameter]:
        """Returns the list of system parameters from the current system parameter file on disk."""
        parameters = []
        r = self.get(urls.API_GET_CURRENT_SYSGEN, group=group)
        if r.status_code == 200:
            for attrs in r.json():
                parameters.append(SystemParameter(attrs))

        return parameters

    def get_active_parameters(self, group: str) -> List[SystemParameter]:
        """Returns the list of system parameters from the active system in memory."""
        parameters = []
        r = self.get(urls.API_GET_ACTIVE_SYSGEN, group=group)
        if r.status_code == 200:
            for attrs in r.json():
                parameters.append(SystemParameter(attrs))

        return parameters

    def edit_parameter(self, source: str, parameter: str, value: str) -> bool:
        """Edits selected system parameters."""
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
