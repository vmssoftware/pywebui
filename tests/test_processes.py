from pytest import fixture, skip

from pywebui.processes import Process


def test_get_process_list(connector):
    assert connector.get_processes()


def test_get_process_details(connector):
    processes = connector.get_processes()

    process = connector.get_process(processes[0].pid)
    assert isinstance(process, Process)
    assert process.pid


@fixture(scope="module")
def ssh_user_pid(connector, auth_username):
    processes = list(filter(lambda p: p.prcnam==auth_username, connector.get_processes()))
    pid = processes[0].pid if processes else None
    if not pid:
        skip('SSH session for user auth_username not found')
    return pid


def test_suspend_process(connector, ssh_user_pid):
    """NOTE: SSH session for user with auth_username is required."""
    connector.suspend_process(ssh_user_pid)
    process = connector.get_process(ssh_user_pid)
    assert process.state == 'SUSP'


def test_resume_process(connector, ssh_user_pid):
    """NOTE: SSH session for user with auth_username is required."""
    connector.resume_process(ssh_user_pid)
    process = connector.get_process(ssh_user_pid)
    assert process.state == 'LEF'


def test_edit_process(connector, ssh_user_pid):
    """NOTE: SSH session for user with auth_username is required."""
    process = connector.get_process(ssh_user_pid)
    prib = process.prib + 1
    connector.edit_process(ssh_user_pid, prib)
    process = connector.get_process(ssh_user_pid)
    assert process.prib == prib


def test_end_process(connector, ssh_user_pid):
    assert connector.end_process(ssh_user_pid)