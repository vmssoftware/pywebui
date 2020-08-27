import time
from pytest import fixture

from pywebui import Connector


HOST = 'http://172.16.1.102:8082/'
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
