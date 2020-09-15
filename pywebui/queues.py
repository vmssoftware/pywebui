from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Queue(ResponseObject):
    pass


class Job(ResponseObject):
    pass


class QueuesMethods:
    def get_batch_queues(self):
        queues = []
        r = self.get(urls.API_GET_BATCH_QUEUES)
        if r.status_code == 200:
            for attrs in r.json():
                queues.append(Queue(attrs))

        return queues

    def get_printer_queues(self):
        queues = []
        r = self.get(urls.API_GET_PRINTER_QUEUES)
        if r.status_code == 200:
            for attrs in r.json():
                queues.append(Queue(attrs))

        return queues

    def get_queue(self, queue):
        r = self.get(urls.API_GET_QUEUE_DETAIL, queue=queue)
        if r.status_code == 200:
            return Queue(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def start_queue(self, queue):
        r = self.put(urls.API_START_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def pause_queue(self, queue):
        r = self.put(urls.API_PAUSE_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def stop_queue(self, queue):
        r = self.put(urls.API_STOP_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_queue_description(self, queue, description):
        r = self.put(urls.API_EDIT_QUEUE_DESCRIPTION, queue=queue, json={"description": description})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def start_job(self, job, queue):
        r = self.put(urls.API_START_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def pause_job(self, job, queue):
        r = self.put(urls.API_PAUSE_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_job(self, job, queue):
        r = self.put(urls.API_DELETE_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
