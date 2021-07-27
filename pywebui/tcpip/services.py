from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Service(ResponseObject):
    """Host object.

    Attributes:
        address (str): the IP address of service.
        name (str): the name of service.
        port (int): the listening port.
        process (str): the name of process for current service.
        protocols: (list(str)): the array of service protocols
        state (str): the state of service.
    """
    def __repr__(self):
        return f"[{self.name}] {self.address}:{self.port}"


class ServiceMethods:
    """Encapsulates methods for manage services."""

    def get_services(self) -> List[Service]:
        """Returns list of services."""
        hosts = []
        r = self.get(urls.API_GET_SERVICES)
        if r.status_code == 200:
            for attrs in r.json():
                hosts.append(Service(attrs))

        return hosts

    def add_service(self, name: str, process: str, port: int, username: str, file: str) -> bool:
        """Creates the new service."""
        data = {
            "name": name,
            "process": process,
            "port": port,
            "username": username,
            "file": file
        }

        r = self.post(urls.API_ADD_SERVICE, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_service(self, name, **kwds) -> bool:
        """Edits the selected service."""
        data = kwds

        r = self.put(urls.API_EDIT_SERVICE, name=name, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_service(self, name: str) -> bool:
        """Delete service."""
        r = self.delete(urls.API_DELETE_SERVICE, name=name)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])