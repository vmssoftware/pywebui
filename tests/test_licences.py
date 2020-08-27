import pytest

from pywebui.licenses import License, LicenseHistory
from pywebui.exceptions import ConnectorException


def test_get_licenses_list(connector):
    assert connector.get_all_licenses()


def test_get_active_licenses_list(connector):
    assert connector.get_active_licenses()


@pytest.fixture(scope="module")
def first_license(connector):
    return connector.get_active_licenses()[0]


def test_get_license_detail(connector, first_license):
    license = connector.get_license(first_license.productName, first_license.authorization)
    assert isinstance(license, License)


@pytest.fixture
def product():
    return 'x25'


@pytest.fixture(scope="function")
def new_license(connector, product):
    data = {
        "issuer": "VSI",
        "authorization": "VSI-CAMERONBRETT-13SEP2019",
        "producer": "VSI",
        "units": 0,
        "termination": 1599955199,
        "options": ["IA64", "PPL"],
        "token": "*** VSI INTERNAL USE ONLY ***",
        "checksum": "2-AKFE-OKFP-CNOC-MKIK"
    }
    connector.delete_license(product, data['authorization'])
    yield connector.register_license(product, data)
    connector.delete_license(product, data['authorization'])


@pytest.mark.skip('Valid license required')
def test_register_license(connector, new_license):
    assert new_license

@pytest.mark.skip('Valid license required')
def test_get_license_history(connector, first_license):
    assert connector.get_license_history(first_license.productName, first_license.authorization)


@pytest.mark.skip('Valid license required')
def test_delete_license(connector, new_license):
    assert connector.delete_license(new_license.productName, new_license.authorization)


@pytest.mark.skip('Valid license required')
def test_export_license_history(connector, new_license):
    content = connector.export_license_history(new_license.productName, new_license.authorization)
    assert content


@pytest.mark.skip('Valid license required')
def test_enable_license(connector, new_license):
    assert connector.enable_license(new_license.productName, new_license.authorization)


@pytest.mark.skip('Valid license required')
def test_disable_license(connector, new_license):
    assert connector.enable_license(new_license.productName, new_license.authorization)


@pytest.mark.skip('Valid license required')
def test_load_license(connector, new_license):
    assert connector.load_license(new_license.productName, new_license.authorization)


@pytest.mark.skip('Valid license required')
def test_unload_license(connector, new_license):
    assert connector.unload_license(new_license.productName, new_license.authorization)
