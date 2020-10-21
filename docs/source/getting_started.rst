Getting Started
===============

To get started using ``PyWebUI`` simply install it with
``pip``::

    $ pip install pywebui

Also you can install ``PyWebUI`` from sources::

    git clone https://github.com/vmssoftware/pywebui.git
    cd webui.connector
    python setup.py install

And then for communication with VMS server do the following::

    import pywebui

    # Create connection object
    c = pywebui.Connector('http://10.11.102.21:8082')
    # Authenticate
    c.login('testuser', 'testuser')
    # Retrieve list of users
    c.get_users()

For handling API errors use `pywebui.exceptions.ConnectorException` class.

Examples
++++++++

Get Users
*********

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    print(c.get_users())


Get User Details
****************

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    print(c.get_user('testuser'))


Create User
***********

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.create_user(
        defprives = ["NETMBX","TMPMBX"],
        device = "SYS$SYSDEVICE",
        directory = "[testuser1]",
        flags = ["DISUSER"],
        owner = "testuser1",
        password = "asd123asd123",
        pwd_expired = 0,
        prives = ["NETMBX","TMPMBX"],
        username = "testuser1",
        uic = ["310","77"]
    )

Edit User
*********

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.edit_user("testuser1",
        owner = "testuser2",
        account="testuser2")


Duplicate User
**************

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.duplicate_user('testuser1', 'testuser2')



Delete User
***********

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.delete_user('testuser1')


Disable User
************

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.disable_user('testuser1')


Enable User
***********

::

    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.enable_user('testuser1')