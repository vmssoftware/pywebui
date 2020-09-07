import os
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

    def get_reports(self):
        return self._get_objects('files', Report)

    def get_scripts(self):
        return self._get_objects('scripts', Script)

    def get_report(self, filename, directory):
        r = self.get(urls.API_GET_REPORT, filename=filename, directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_log(self, filename, directory):
        r = self.get(urls.API_GET_REPORT_LOG, filename=os.path.basename(filename), directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def generate(self, script_dir, script_name, report_dir):
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

    def export_report(self, filename, directory):
        r = self.get(urls.API_EXPORT_REPORT, filename=filename, directory=directory)
        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])