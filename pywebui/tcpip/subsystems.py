from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Subsystem(ResponseObject):
    """Host object.

    Attributes:
        configured (bool): the subsystem is configured or not (boolean value).
        display (bool): display this subsystem in WebUI or not (boolean value). The true for subsystems “inet”, “net” and “socket”, for other - false.
        name (str): the name of subsystem.
        status (str): the status of subsystem.
    """
    def __repr__(self):
        return self.name


class SubsystemMethods:
    """Encapsulates methods for manage subsystems."""

    def get_subsystems(self) -> List[Subsystem]:
        """Returns list of subsystems."""
        hosts = []
        r = self.get(urls.API_GET_SUBSYSTEMS)
        if r.status_code == 200:
            for attrs in r.json():
                hosts.append(Subsystem(attrs))

        return hosts

    def get_subsystem(self, name) -> Subsystem:
        """Returns the information about configuration of selected subsystem."""
        r = self.get(urls.API_GET_SUBSYSTEM, name=name)
        if r.status_code == 200:
            return Subsystem(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_subsystem(self, name: str, attribute: str, value: int) -> bool:
        """Edits the current value of attribute for selected subsystem."""
        data = {
            "name": attribute,
            "value": value
        }

        r = self.put(urls.API_EDIT_SUBSYSTEMS, name=name, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
