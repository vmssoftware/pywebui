from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Interface(ResponseObject):
    """Interface object.

    Attributes:
        address (str): the IP address of interface.
        intf (str): the name of interface.
        mask (str): the network mask.
        mtu (int): the maximum transmission unit (MTU) size.
        pkt_recv (int): the received packets.
        pkt_sent (int): the sent packets.
    """
    def __repr__(self):
        return f"[{self.intf}] {self.address}"


class InterfaceMethods:
    """Encapsulates methods for manage interfaces."""
    def get_interfaces(self) -> List[Interface]:
        """Returns the list of all interfaces."""
        devices = []
        r = self.get(urls.API_GET_INTERFACES)
        if r.status_code == 200:
            for attrs in r.json():
                devices.append(Interface(attrs))

        return devices

    def get_interface(self, name) -> Interface:
        """Returns details for selected interface."""
        r = self.get(urls.API_GET_INTERFACE, name=name)
        if r.status_code == 200:
            return Interface(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])