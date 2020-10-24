import os
from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Report(ResponseObject):
    """Report object.

    Attributes:
        date (int): The date of creating report or date of last edition of script (Unix Epoch format).
        user (str): The name of user who edit.
        fileName (str): The name of report or script.
        directory (str): The directory name
    """
    def __repr__(self):
        return self.fileName


class Script(Report):
    """Script object.

    Attributes:
        date (int): The date of creating report or date of last edition of script (Unix Epoch format).
        user (str): The name of user who edit.
        fileName (str): The name of report or script.
        directory (str): The directory name
    """


class ReportMethods:
    """Encapsulates methods for manage reports."""

    def _get_objects(self, attr, _class):
        objects = []
        r = self.get(urls.API_GET_REPORTS)

        if r.status_code == 200:
            classname = attr[:-1].capitalize()
            for directory, items in r.json()[attr].items():
                for attrs in items:
                    attrs.update({'directory': directory})
                    obj = _class(attrs)
                    objects.append(obj)
        else:
            message = r.json()
            raise ConnectorException(message['details'])

        return objects

    def get_reports(self) -> List[Report]:
        """Returns the list of reports."""
        return self._get_objects('files', Report)

    def get_scripts(self) -> List[Script]:
        """Returns the list of scripts."""
        return self._get_objects('scripts', Script)

    def get_report(self, filename: str, directory: str) -> str:
        """Returns  details of report."""
        r = self.get(urls.API_GET_REPORT, filename=filename, directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_log(self, filename: str, directory: str) -> str:
        """Returns details of log file."""
        r = self.get(urls.API_GET_REPORT_LOG, filename=os.path.basename(filename), directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def generate(self, script_dir: str, script_name: str, report_dir: str) -> bool:
        """Runs script to generate report."""
        data = [{
            "scriptDir": script_dir,
            "scriptName": script_name,
            "fileDir": report_dir
        }]
        r = self.post(urls.API_GENERATE_REPORTS, json=data)
        if r.status_code == 200:
            return True
        else:
            return False

    def export_report(self, filename: str, directory: str) -> str:
        """Returns report content."""
        r = self.get(urls.API_EXPORT_REPORT, filename=filename, directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])