import random

import pytest

from pywebui.exceptions import ConnectorException
from pywebui.identifiers import Identifier


@pytest.fixture
def identifier_name():
    return 'TESTIDENTIFIER'


@pytest.fixture(scope="function")
def new_identifier(connector, identifier_name):
    try:
        connector.delete_identifier(identifier_name)
    except ConnectorException:
        pass

    identifier_value = random.randint(65536, 16777215)
    identifier_type = random.choice(Identifier.TYPES)
    identifier_attributes = random.sample(Identifier.ATTRIBUTES, 2)

    created = connector.create_identifier(
        identifier_name,
        identifier_value,
        identifier_type,
        identifier_attributes)

    yield connector.get_identifier(identifier_name)

    try:
        connector.delete_identifier(identifier_name)
    except ConnectorException:
        pass


def test_get_identifiers(connector):
    assert connector.get_identifiers()


def test_get_identifier(connector, new_identifier):
    assert connector.get_identifier(new_identifier.name)


def test_get_all_identifiers(connector):
    assert connector.get_all_identifiers()


def test_get_identifier_holders(connector):
    assert connector.get_identifier_holders(identifier='WEBUI_READ')


def test_create_identifier(connector, new_identifier):
    pass


def test_delete_identifier(connector, new_identifier):
    assert connector.delete_identifier(new_identifier.name)


def test_grant_identifier(connector, user, new_identifier):
    assert connector.grant_identifiers(user.username, [new_identifier.name])


def test_rovoke_identifiers(connector, user, new_identifier):
    connector.grant_identifiers(user.username, [new_identifier.name])
    assert connector.get_holder_identifiers(user.username)

    assert connector.rovoke_identifiers(user.username, [new_identifier.name])
    assert len(connector.get_holder_identifiers(user.username)) == 0


def test_get_holder_identifiers(connector, user, new_identifier):
    connector.grant_identifiers(user.username, [new_identifier.name])

    assert connector.get_holder_identifiers(holder=user.username)