from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Report(ResponseObject):
    def __repr__(self):
        return self.fileName


class Script(Report):
    pass


class ReportMethods:
    pass