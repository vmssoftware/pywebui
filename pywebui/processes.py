from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Process(ResponseObject):
    def __repr__(self):
        return self.pid


class ProcessMethods:
    def get_processes(self):
        processes = []
        r = self.get(urls.API_GET_PROCESS_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                processes.append(Process(attrs))

        return processes

    def get_process(self, pid):
        r = self.get(urls.API_GET_PROCESS_DETAIL, pid=pid)
        if r.status_code == 200:
            return Process(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def end_process(self, pid):
        r = self.post(urls.API_KILL_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_process(self, pid, prib):
        r = self.put(urls.API_EDIT_PROCESS, pid=pid, json={"prib": prib})
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def suspend_process(self, pid):
        r = self.put(urls.API_SUSPEND_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def resume_process(self, pid):
        r = self.put(urls.API_RESUME_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])
