def test_get_subsystems(connector):
    assert connector.get_subsystems()


def test_get_subsystem(connector):
    assert connector.get_subsystem('inet')


def test_get_subsystem_attribute(connector):
    subsystem = connector.get_subsystem('inet')
    assert subsystem.get_attribute('icmp_redirecttimeout')


def test_edit_subsystem(connector):
    subsystem = connector.get_subsystem('inet')
    attribute = subsystem.get_attribute('icmp_redirecttimeout')
    old_value = attribute.currentValue
    new_value = attribute.minValue

    assert connector.edit_subsystem(subsystem.name, attribute.name, new_value)
    subsystem = connector.get_subsystem('inet')
    attribute = subsystem.get_attribute('icmp_redirecttimeout')
    assert attribute.currentValue == new_value

    assert connector.edit_subsystem(subsystem.name, attribute.name, old_value)
    subsystem = connector.get_subsystem('inet')
    attribute = subsystem.get_attribute('icmp_redirecttimeout')
    assert attribute.currentValue == old_value
