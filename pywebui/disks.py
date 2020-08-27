from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Disk(ResponseObject):
    def __repr__(self):
        return self.displayDevName


class DiskMethods:
    def get_disks(self):
        disks = []
        r = self.get(urls.API_GET_DISKS)
        if r.status_code == 200:
            for attrs in r.json():
                disks.append(Disk(attrs))

        return disks

    def get_disk(self, device):
        r = self.get(urls.API_GET_DISK_DETAIL, device=device)
        if r.status_code == 200:
            return Disk(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])
