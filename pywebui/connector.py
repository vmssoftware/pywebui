import requests
from urllib.parse import urljoin

from pywebui import urls
from pywebui.users import UserMethods
from pywebui.system import SystemMethods
from pywebui.processes import ProcessMethods
from pywebui.licenses import LicenseMethods
from pywebui.disks import DiskMethods
from pywebui.cluster import ClusterMethods
from pywebui.reports import ReportMethods
from pywebui.packages import InstalledPackagesMethods
from pywebui.parameters import SystemParametersMethods
from pywebui.identifiers import IdentifiersMethods
from pywebui.queues import QueuesMethods


class Connector(
    UserMethods,
    SystemMethods,
    ProcessMethods,
    LicenseMethods,
    DiskMethods,
    ClusterMethods,
    ReportMethods,
    InstalledPackagesMethods,
    SystemParametersMethods,
    IdentifiersMethods,
    QueuesMethods
):
    token = None

    def __init__(self, host):
        self.host = host
        self.session = requests.Session()

    def login(self, username, password):
        url = urljoin
        r = self.session.get(urljoin(self.host, urls.API_LOGIN), auth=(username, password))
        if r.status_code == 200:
            if 'jwt' in r.cookies:
                self.token = r.cookies['jwt']

    def get(self, url, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.get(url, cookies={'jwt': self.token})
        return response

    def post(self, url, json={}, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.post(url, json=json, cookies={'jwt': self.token})
        return response

    def put(self, url, json={}, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.put(url, json=json, cookies={'jwt': self.token})
        return response

    def delete(self, url, **query_params):
        url = urljoin(self.host, url.format(**query_params))
        response = self.session.delete(url, cookies={'jwt': self.token})
        return response

    def get_version(self):
        r = self.get(urls.API_GET_VERSION)

        if r.status_code == 200:
            return r.json().get('version', None)