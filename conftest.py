import time
from pytest import fixture

from pywebui import Connector


HOST = 'http://10.11.102.21:8082/'
USERNAME = 'TESTUSER'
PASSWORD = 'testuser'


@fixture
def hostname():
    return HOST


@fixture(scope="session")
def auth_username():
    return USERNAME


@fixture(scope="session")
def connector():
    c = Connector(HOST)
    c.login(USERNAME, PASSWORD)
    time.sleep(1)
    return c


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
