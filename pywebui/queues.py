from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Queue(ResponseObject):
    """Queue object.

    Attributes:
        description (str): The text that describes the specified queue.
        executingJobCount (int): The number of jobs in the queue that are currently executing.
        holdingJobCount (int): The number of jobs in the queue being held until explicitly released.
        jobCount (int): The total amount of jobs (jobCount = executingJobCount + holdingJobCount + pendingJobCount + retainedJobCount + timedReleaseJobCount).
        jobLimit (int): The maximum number of jobs that can execute simultaneously on a queue.
        mountedForm (str): The name of the specified form or the mounted form associated with the specified job or queue. Contains also the name of the paper stock on which the specified form is to be printed (using for printer queues).
        nodeName (str): The name of the node.
        pendingJobCount (int): The number of jobs in the queue in a pending state.
        retain (str): The circumstances under which you want your jobs to be retained in a queue.
        retainedJobCount (int): The number of jobs in the queue retained after successful completion plus those retained on error.
        status (dict): The queue’s status.
        timedReleaseJobCount (int): The number of jobs in the queue on hold until a specified time.
        queueName (str): The name of queue.
        queueType (str): The type of queue.
    """


class QueueDetails(Queue):
    """
    QueueDetails object.

    Attributes:
        autostartOn (str): The names of the nodes on which the specified autostart queue can be run.
        basePriority (int): The priority at which batch jobs are initiated from a batch execution queue or the priority of symbiont process that controls output execution queues.
        default (str): The text that describes the specified queue.
        description (str): The text that describes the specified queue.
        enableGeneric (str): Is the queue an execution queue that can accept work from a generic queue.
        jobLimit (int): The maximum number of jobs that can execute simultaneously on a queue.
        jobs (list(str)): The array of jobs, contains list of jobs with details information.
        library (str): The name of the device control library for the queue.
        mountedForm (str): The name of the specified form or the mounted form associated with the specified job or queue. Contains also the name of the paper stock on which the specified form is to be printed (using for printer queues).
        nodeName (str): The name of the node on which the execution queue is located.
        options (list(str)): The queue’s option array, which contains option information.
        owner (str): The owner name of the queue.
        processor (str): The name of the symbiont image that executes print jobs initiated from the queue.
        protection (str): The string with queue protection information.
        queueName (str): The name of queue.
        schedule (str): The information if jobs initiated from the queue are scheduled according to size, with the smallest job of a given priority processed first.
        separate (str): The string with queue settings.
        status (dict): The queue’s status object, which contains details of status.
    """


class Job(ResponseObject):
    """Job object.

    Attributes:
        description (str): The text that describes the specified job.
        entry (int): The queue entry number of the job.
        files list((str)): The array of names which are contained in the job.
        jobName (str): The name of the job.
        jobSize (int): The total number of disk blocks in the print job.
        note (str): The note that is to be printed on the job flag and file flag pages of the job.
        status (dict): The job’s status object, which contains details of status.
        userName (str): The user name of the owner of the job.
    """


class QueuesMethods:
    """Encapsulates methods for manage queues."""

    def get_batch_queues(self) -> List[Queue]:
        """Returns the list of batch queues."""
        queues = []
        r = self.get(urls.API_GET_BATCH_QUEUES)
        if r.status_code == 200:
            for attrs in r.json():
                queues.append(Queue(attrs))

        return queues

    def get_printer_queues(self) -> List[Queue]:
        """Returns the list of printer queues."""
        queues = []
        r = self.get(urls.API_GET_PRINTER_QUEUES)
        if r.status_code == 200:
            for attrs in r.json():
                queues.append(Queue(attrs))

        return queues

    def get_queue(self, queue: str) -> QueueDetails:
        """Returns the details of selected queue."""
        r = self.get(urls.API_GET_QUEUE_DETAIL, queue=queue)
        if r.status_code == 200:
            return Queue(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def start_queue(self, queue: str) -> bool:
        """Starts selected queue."""
        r = self.put(urls.API_START_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def pause_queue(self, queue: str) -> bool:
        """Pauses selected queue."""
        r = self.put(urls.API_PAUSE_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def stop_queue(self, queue: str) -> bool:
        """Stops selected queue."""
        r = self.put(urls.API_STOP_QUEUE, queue=queue)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_queue_description(self, queue: str, description: str) -> bool:
        """Edits description of selected queue."""
        r = self.put(urls.API_EDIT_QUEUE_DESCRIPTION, queue=queue, json={"description": description})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def start_job(self, job: str, queue: str) -> bool:
        """Starts selected job in queue."""
        r = self.put(urls.API_START_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def pause_job(self, job: str, queue: str) -> bool:
        """Pauses selected job in queue.

        Job gets status “Holding” and retain in queue until release."""
        r = self.put(urls.API_PAUSE_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_job(self, job: str, queue: str) -> bool:
        """Deletes selected job from queue."""
        r = self.put(urls.API_DELETE_JOB, job=job, json={"queueName": queue})

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])
