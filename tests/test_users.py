from pytest import fixture, raises

from pywebui.users import User
from pywebui.exceptions import ConnectorException


@fixture
def tmp_username():
    return 'TESTAPIUSER'


@fixture(scope="function")
def user(connector, tmp_username):
    connector.delete_user(tmp_username)
    user = connector.create_user(
        username=tmp_username,
        owner=tmp_username,
        password="asd123asd123",
        uic=("312", "77"),
        def_priv=["NETMBX","TMPMBX"],
        device="SYS$SYSDEVICE",
        directory=f"[{tmp_username}]",
        pwd_expired=False,
        priv=["NETMBX","TMPMBX"],
        flags=["DISUSER"],
    )
    yield user
    connector.delete_user(tmp_username)


def test_get_users_list(connector):
    assert connector.get_users()


def test_get_user_detail(connector, user):
    user = connector.get_user(user.username)
    assert isinstance(user, User)
    assert user.username == user.username


def test_create_user(connector, user):
    user = connector.get_user(user.username)
    assert isinstance(user, User)
    assert user.username == user.username


def test_edit_user(connector, user):
    assert connector.edit_user(user,
        owner = f"{user.username}X")


def test_delete_user(connector, user):
    assert connector.delete_user(user.username)
    with raises(ConnectorException):
        connector.get_user(user.username)


def test_dublicate_user(connector, auth_username, tmp_username):
    assert connector.duplicate_user(auth_username, tmp_username, ("200", "500"))
    user = connector.get_user(tmp_username)
    assert user.username == tmp_username
    assert connector.delete_user(tmp_username)


def test_enable_user(connector, user):
    assert connector.enable_user(user.username)
    user = connector.get_user(user.username)
    assert len(user.flags) == 0

    assert connector.disable_user(user.username)
    user = connector.get_user(user.username)
    assert 'DISUSER' in user.flags