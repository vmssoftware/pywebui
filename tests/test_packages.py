import pytest


def test_get_installed_packages(connector):
    assert connector.get_installed_packages()


def test_get_package_history(connector):
    package = connector.get_installed_packages()[0]
    assert connector.get_package_history(package.name)


def test_export_package_history(connector):
    package = connector.get_installed_packages()[0]
    assert connector.export_package_history(package.name)


@pytest.mark.skip('Exact project should be specified')
def test_delete_package(connector):
    package = connector.get_installed_packages()[0]
    assert connector.delete_package(package.name)