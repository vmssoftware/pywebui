from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Process(ResponseObject):
    """Process object.

    Attributes:
        bufio (int): The сount of the buffered I/O operations of the process.
        cputim (int): The process’s accumulated CPU time in 10-millisecond 'ticks'.
        dirio (int): The count of the direct I/O operations of the process.
        pageflts (int): The total number of page faults incurred by the process.
        pid (str): The process identification (PID) of the process.
        prcnam (str): The name of the process.
        pri (int): The current priority of the process.
        state (str): The state of the process.
        virtpeak (int): The peak virtual address size in pagelets of the process.
    """
    def __repr__(self):
        return self.pid


class ProcessDetails(Process):
    """Process details object.

        aptcnt (int): The active page table count of the process.
        astcnt (int): The count of the remaining AST quota.
        astlm (int): The AST limit quota of the process.
        biocnt (int): The count of the remaining buffered I/O quota.
        biolm (int): The buffered I/O limit quota of the process.
        bufio (int): The сount of the buffered I/O operations of the process.
        bytcnt (int): The remaining buffered I/O byte count quota of the process.
        bytlm (int): The buffered I/O byte count limit quota of the process.
        cpu_id (int): The ID of the CPU on which the process is running or on which it last ran.
        cputim (int): The process’s accumulated CPU time in 10-millisecond 'ticks'.
        diocnt (int): The remaining direct I/O quota of the process.
        diolm (int): The direct I/O quota limit of the process.
        dirio (int): The count of the direct I/O operations of the process.
        enqcnt (int): The remaining lock request quota of the process.
        enqlm (int): The lock request quota of the process.
        filcnt (int): The remaining open file quota of the process.
        fillm (int): The open file limit quota of the process.
        freptecnt (int): The number of pagelets that the process has available for virtual memory expansion.
        gpgcnt (int): The process's global page count in the working set.
        grp (int): The group number of the process's UIC.
        imagname (str): The directory specification and the image file name.
        jobprccnt (int): The total number of sub-processes owned by the job.
        nodename (str): The name of node.
        owner (int): The process identification (PID) of the process that created the specified process (process owner).
        pageflts (int): The total number of page faults incurred by the process.
        pagfilcnt (int): The remaining paging file quota of the process.
        pgflquota (int): The paging file quota (maximum virtual page count) of the process.
        pid (str): The process identification (PID) of the process.
        ppgcnt (int): The number of pagelets the process has in the working set.
        prccnt (int): The number of sub-processes created by the process.
        prclm (int): The sub-process quota of the process.
        prcnam (str): The name of the process.
        pri (int): The current priority of the process.
        prib (int): The base priority of the process (value in range 0 through 31).
        procpriv (list(str)): The default privileges of the process.
        state (str): The state of the process.
        sts (list(str)): The statuses of the process.
        tqcnt (int): The remaining timer queue entry quota of the process.
        tqlm (int): The process's limit on timer queue entries.
        uic (list(str)): The UIC of the process. Format UIC - [Group, Member]
        uic_str (str): The UIC of the process (in word strings).
        username (str): The user name of the process.
        virtpeak (int): The peak virtual address size in pagelets of the process.
    """


class ProcessMethods:
    def get_processes(self) -> List[Process]:
        """Get the list of processes."""
        processes = []
        r = self.get(urls.API_GET_PROCESS_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                processes.append(Process(attrs))

        return processes

    def get_process(self, pid: str) -> List[ProcessDetails]:
        """Get details of selected process.

        Args:
            pid (str): The PID of selected process."""
        r = self.get(urls.API_GET_PROCESS_DETAIL, pid=pid)
        if r.status_code == 200:
            return ProcessDetails(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def end_process(self, pid: str) -> bool:
        """Ends selected process.

        Args:
            pid (str): The PID of selected process."""
        r = self.post(urls.API_KILL_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def edit_process(self, pid: str, prib: int) -> bool:
        """Edits selected process. In current moment we can edit only the base priority of process.

        Args:
            pid (str): The PID of selected process.
            prib (int): The base priority of process.
        """
        r = self.put(urls.API_EDIT_PROCESS, pid=pid, json={"prib": prib})
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def suspend_process(self, pid: str) -> bool:
        """Suspends selected process.

        Args:
            pid (str): The PID of selected process."""
        r = self.put(urls.API_SUSPEND_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def resume_process(self, pid: str) -> bool:
        """Resumes selected process.

        Args:
            pid (str): The PID of selected process."""
        r = self.put(urls.API_RESUME_PROCESS, pid=pid)
        if r.status_code == 200:
            return True
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])
