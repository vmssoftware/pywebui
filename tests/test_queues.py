import pytest

from pywebui.exceptions import ConnectorException


@pytest.fixture
def queue_name():
    return 'TEST_POSTMAN'


@pytest.fixture
def job_name():
    return 'TEST_BATCH_1MIN'


@pytest.fixture
def job_id():
    return 212


def test_get_batch_queues(connector):
    assert connector.get_batch_queues()


def test_get_queue(connector, queue_name):
    assert connector.get_queue(queue_name)


def test_get_queue(connector, queue_name):
    assert connector.get_queue(queue_name)


def test_start_queue(connector, queue_name):
    assert connector.start_queue(queue_name)


def test_pause_queue(connector, queue_name):
    assert connector.pause_queue(queue_name)


def test_stop_queue(connector, queue_name):
    assert connector.stop_queue(queue_name)


def test_edit_queue_description(connector, queue_name):
    assert connector.edit_queue_description(queue_name, 'Some test description')


def test_start_job(connector, job_id, queue_name):
    assert connector.start_job(job_id, queue_name)


def test_pause_job(connector, job_id, queue_name):
    assert connector.pause_job(job_id, queue_name)


def test_delete_job(connector, job_id, queue_name):
    assert connector.delete_job(job_id, queue_name)
