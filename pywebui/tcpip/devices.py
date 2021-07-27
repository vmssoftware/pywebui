from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Device(ResponseObject):
    """Device object.

    Attributes:
        deviceSocket (str): the device socket.
        localPort (int): the local port of device.
        remoteHost (str): the remote host of device.
        remotePort (int): the remote port of device.
        service (str): the service of device.
        type (str): the type of device.
    """
    def __repr__(self):
        return f"[{self.service}] {self.deviceSocket}"


class DeviceMethods:
    """Encapsulates methods for manage devices."""

    def get_devices(self) -> List[Device]:
        """Returns the list of all devices."""
        devices = []
        r = self.get(urls.API_GET_DEVICES)
        if r.status_code == 200:
            for attrs in r.json():
                devices.append(Device(attrs))

        return devices

    def get_device(self, name) -> Device:
        """Returns details for selected device."""
        r = self.get(urls.API_GET_DEVICE, name=name)
        if r.status_code == 200:
            return Device(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])