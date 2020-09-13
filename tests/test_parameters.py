import pytest


def test_get_current_parameters(connector):
    assert connector.get_current_parameters(group='ALL')


def test_get_active_parameters(connector):
    assert connector.get_active_parameters(group='ALL')


@pytest.mark.skip('Exact parameter should be specified')
def test_edit_parameter(connector):
    parameters = connector.get_current_parameters(group='ALL')
    parameter = list(filter(lambda p: p.name == 'USER3', parameters))[0]
    assert connector.edit_parameter(source='current', parameter=parameter.name, value=1)