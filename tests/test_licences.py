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
    return 'X25'


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
    try:
        connector.delete_license(product, data['authorization'])
    except ConnectorException:
        pass

    yield connector.register_license(product, data)

    try:
        connector.delete_license(product, data['authorization'])
    except ConnectorException:
        pass


def test_register_license(connector, new_license):
    assert new_license


def test_get_license_history(connector, new_license):
    connector.disable_license(new_license.productName, new_license.authorization)
    assert connector.get_license_history(new_license.productName, new_license.authorization)


def test_delete_license(connector, new_license):
    assert connector.delete_license(new_license.productName, new_license.authorization)


def test_export_license_history(connector, new_license):
    connector.disable_license(new_license.productName, new_license.authorization)
    content = connector.export_license_history(new_license.productName, new_license.authorization)
    assert content


def test_enable_license(connector, new_license):
    assert connector.enable_license(new_license.productName, new_license.authorization)


def test_disable_license(connector, new_license):
    assert connector.disable_license(new_license.productName, new_license.authorization)


def test_load_license(connector, new_license):
    assert connector.load_license(new_license.productName, new_license.authorization)


def test_unload_license(connector, new_license):
    assert connector.unload_license(new_license.productName, new_license.authorization)
