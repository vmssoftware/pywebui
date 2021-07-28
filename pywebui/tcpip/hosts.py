from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Host(ResponseObject):
    """Host object.

    Attributes:
        address (str): the IP address of host.
        aliases (list(str)): the array with aliases of host.
        name (str): the name of host.
    """
    def __repr__(self):
        return self.name


class HostMethods:
    """Encapsulates methods for manage hosts."""

    def get_hosts(self) -> List[Host]:
        """Returns list of hosts."""
        hosts = []
        r = self.get(urls.API_GET_HOSTS)
        if r.status_code == 200:
            for attrs in r.json():
                hosts.append(Host(attrs))

        return hosts

    def add_host(self, name: str, address: str, aliases: List[str] = None) -> bool:
        """Creates the new host."""
        data = {
            'address': address,
            'name': name,
            'aliases': [] if aliases is None else aliases}

        r = self.post(urls.API_ADD_HOST, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_host_aliases(self, name: str, address: str, aliases: List[str] = None) -> bool:
        """Edits aliases of the selected host."""
        data = {
            'aliases': [] if aliases is None else aliases}

        r = self.put(urls.API_EDIT_HOST, name=name, address=address, json=data)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_host(self, name: str, address: str) -> bool:
        """Delete host."""
        r = self.delete(urls.API_DELETE_HOST, name=name, address=address)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])