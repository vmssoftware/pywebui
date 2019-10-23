import pywebui

HOST = 'http://10.11.102.21:8082'

def test_constructor():
    c = pywebui.Connector(HOST)

def test_auth():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')

def test_get_users_list():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.get_users())

def test_get_user_detail():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.get_user('testuser'))

def test_create_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    c.delete_user('testuser7')
    c.create_user(
        username="testuser7",
        owner="testuser7",
        password="asd123asd123",
        uic=["312", "77"],
        def_priv = ["NETMBX","TMPMBX"],
        device = "SYS$SYSDEVICE",
        directory = "[testuser7]",
        pwd_expired=0,
        priv = ["NETMBX","TMPMBX"],
        flags=["DISUSER"],
        # account = "testuser5",
    )

def test_edit_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    c.edit_user("testuser1", owner = "testuser2", account="testuser2")

def test_delete_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    c.delete_user('testuser1')

def test_dublicate_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.duplicate_user('testuser1', 'testuser2'))

def test_enable_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    c.enable_user('testuser3')

def test_disable_user():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    c.disable_user('testuser3')

def test_get_sysinfo():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.get_sysinfo())

def test_get_resinfo():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.get_resinfo())

def test_get_process_list():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    print(c.get_processes())

def test_get_process_details():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    processes = c.get_processes()

    print(c.get_process(processes[0].pid))

def test_end_process():
    c = pywebui.Connector(HOST)
    c.login('testuser', 'testuser')
    processes = c.get_processes()

    print(c.end_process(processes[0].pid))
