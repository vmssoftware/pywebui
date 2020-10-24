from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class SysInfo(ResponseObject):
    """Resource information object.

    Attributes:
        arch_name (str): The name of the CPU architecture on which the process is executing.
        boottime (int): The time when the node was booted (Unix Epoch format).
        hw_name (str): The model name string of the node.
        nodename (str): The name of the node.
        serial_number (str): The system serial number from out of the Hardware Restart Parameter Block (HWRPB).
        version (str): The software version number of the OpenVMS operating system running on the node.
    """

class ResInfo(ResponseObject):
    """Resource information object.

    Attributes:
        activeCPUCount (int): The active CPU count.
        bufio (int): The number of buffered I/Os.
        cef (int): The number of processes in the common event flag wait state.
        clk_tck (int): The number of CPU/core 'ticks' per second.
        colpg (int): The number of processes in the collided page wait state.
        com (int): The number of processes in the computable state.
        como (int): The number of outswapped processes in the computable state.
        cpuexec (int): The amount of time, in 10-millisecond units, spent by all CPUs in executive mode.
        cpuidle (int): The amount of time, in 10-millisecond units, spent by all CPUs in idle mode.
        cpuintstk (int): The amount of time, in 10-millisecond units, spent by all CPUs in processing interrupts.
        cpukernel (int): The amount of time, in 10-millisecond units, spent by all CPUs in kernel mode.
        cpumpsynch (int): The amount of time, in 10-millisecond units, spent by the primary CPU in synchronization mode.
        cpusuper (int): The amount of time, in 10-millisecond units, spent by all CPUs in supervisor mode.
        cpuuser (int): The amount of time, in 10-millisecond units, spent by all CPUs in user mode.
        cputotal (int): The total amount of time, in 10-millisecond units, spent by all CPUs (cputotal = cpuintstk + cpumpsynch + cpukernel + cpuexec + cpusuper + cpuuser + cpuidle).
        cur (int): The number of currently-executing processes.
        dirio (int): The number of direct I/Os.
        fpg (int): The number of processes in the free page wait state.
        frlist (int): The number of pages on the free list.
        hib (int): The number of processes in the hibernate state.
        hibo (int): The number of outswapped processes in the hibernate state.
        lef (int): The number of processes in the local event flag wait state.
        lefo (int): The number of outswapped processes in the local event flag wait state.
        memtotal (int): The total number of kilobytes of physical memory in the system configuration.
        memuse (int): The number of kilobytes of using physical memory in the system configuration.
        modlist (int): The number of pages on the modified page list.
        mwait (int): The number of processes in the miscellaneous resource wait state.
        nproc (int): The number of online/active CPU's/cores.
        other (int): The sum of processes in the common event flag wait, in the collided page wait, in the free page wait, in the suspended states and out swapped processes in the suspended state.
        pfw (int): The number of processes in the page fault wait state.
        susp (int): The number of processes in the suspended state.
        suspo (int): The number of outswapped processes in the suspended state.
        time (int): The current system time is the number of seconds since November 17, 1858 (Unix Epoch format).
        total (int): The total number of processes.
    """


class SystemMethods:
    def get_sysinfo(self) -> SysInfo:
        """Returns the system information."""
        r = self.get(urls.API_GET_SYSTEM_INFO)

        if r.status_code == 200:
            return SysInfo(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_resinfo(self) -> ResInfo:
        """Returns the information about resources of node."""
        r = self.get(urls.API_GET_SYSTEM_RESOURCES)

        if r.status_code == 200:
            return ResInfo(r.json())
        else:
            message = r.json()
            raise ConnectorException(message['details'])
