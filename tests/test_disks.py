def test_get_disks(connector):
    assert connector.get_disks()


def test_get_disk(connector):
    disk = connector.get_disks()[0]
    assert connector.get_disk(disk.deviceName)