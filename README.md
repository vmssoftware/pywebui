# PyWebUI: Python bind for OpenVMS Administration Tool

## Installation

```bash
git clone https://vikonnikov@bitbucket.org/vms_software/webui.connector.git
cd webui.connector
python setup.py install
```

## Usage

```python
# Import library
import pywebui

# Create connection object
c = pywebui.Connector('http://10.11.102.21:8082')
# Authenticate
c.login('testuser', 'testuser')
# Retrieve list of users
c.get_users()
```

## Examples

### Get Users

```python
     c = pywebui.Connector('http://10.11.102.21:8082')
     c.login('testuser', 'testuser')
     print(c.get_users())
```

### Get User Details

```python
     c = pywebui.Connector('http://10.11.102.21:8082')
     c.login('testuser', 'testuser')
     print(c.get_user('testuser'))
```

### Create User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.create_user(
        def_priv = ["NETMBX","TMPMBX"],
        device = "SYS$SYSDEVICE",
        directory = "[testuser1]",
        flags = ["DISUSER"],
        owner = "testuser1",
        password = "asd123asd123",
        pwd_expired = 0,
        priv = ["NETMBX","TMPMBX"],
        username = "testuser1",
        uic = ["310","77"]
        # account = "testusr1",
    )
```

### Edit User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.edit_user("testuser1",
        owner = "testuser2",
        account="testusr2")
```

### Duplicate User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.duplicate_user('testuser1', 'testuser2', ["312","77"])
```


### Delete User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.delete_user('testuser1')
```

### Disable User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.disable_user('testuser1')
```

### Enable User

```python
    c = pywebui.Connector('http://10.11.102.21:8082')
    c.login('testuser', 'testuser')
    c.enable_user('testuser1')
```