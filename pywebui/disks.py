from typing import List

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Disk(ResponseObject):
    """Storage object.

    Attributes:
        alloClass (int): the allocation class of the host.
        availablePathCount (int): the number of available, working paths for a multipath-capable device.
        clusterSize (int): the volume cluster size.
        defBufSize (int): the default buffer size.
        devChars (dict): device-independent characteristics object.
        devDescription (str): the description of device options.
        deviceName (str): the disk name.
        devProt (str): the protection data of the device.
        displayDevName (str): extended disk name.
        errСnt (int): the error count of the disk.

        expSizeLimit (list(str)): the current expansion limit on the volume object, which contains two fields:
                     blocks - the current expansion limit on the volume in blocks (one block is 512 bytes).
                     bytes - the current expansion limit on the volume in bytes.

        extendQuantity (int): the default extension size for all files on the volume.
        fastPath (int): is unit supports FAST PATH Affinity.

        freeSpace (list(str)): the free space object, which contains two fields:
                      blocks - the number of free blocks on a disk (one block is 512 bytes).
                      bytes - the number of free bytes on a disk.

        hostName (str): the name of the host serving the primary path.

        logVolSize (list(str)): the current logical volume size of the volume object, which contains two fields:
                     blocks - the current logical volume size in blocks (one block is 512 bytes).
                     bytes - the current logical volume size in bytes.

        maxFilesAllowed (int): the maximum number of files on the volume.
        mountСnt (int): the number of times the volume has been mounted on the local system.
        mountStatus (str): the mount status of the volume.
        opCnt (int): the operation count of the disk.
        ownerPID (str): the process identification (PID) of the owner of the device.
        ownerProcess (str): the owner of the disk.
        ownerUIC (str): the user identification code (UIC) of the owner of the device as a string.
        prefCPU (int): the preferred CPU.
        refCnt (int): the number of channels assigned to the disk.
        relVolNumber (int): the volume number of this volume in the volume set.
        secPerTrack (int): the number of sectors per track.
        totalCyls (int): the number of cylinders on the volume.

        totalSize (list(str)): the maximum size on the volume object, which contains two fields:
                     blocks - the maximum size on the volume in blocks (one block is 512 bytes).
                     bytes - the maximum size on the volume in bytes.

        transСnt (int): the transaction count for the volume.
        trPerCyl (int): the number of tracks per cylinder.
        volDescription (str): the description of volume options.
        volName (str): the volume name.
        volOwnerUIC (str): the user identification code (UIC) of the owner of the volume as a string
        volProt (str): the protection data of the volume.
        wwid (str): the World Wide Identifier (WWID) of the disk.
    """
    def __repr__(self):
        return self.displayDevName


class DiskMethods:
    """Encapsulates methods for manage storage."""

    def get_disks(self) -> List[Disk]:
        """Returns the list of all disks."""
        disks = []
        r = self.get(urls.API_GET_DISKS)
        if r.status_code == 200:
            for attrs in r.json():
                disks.append(Disk(attrs))

        return disks

    def get_disk(self, device) -> Disk:
        """Returns details for selected disk."""
        r = self.get(urls.API_GET_DISK_DETAIL, device=device)
        if r.status_code == 200:
            return Disk(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])
