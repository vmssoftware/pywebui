PyWebUI: Python bind for OpenVMS Administration Tool
========================================================

Installation
------------

Usage
-----
#  
```python
# Create connection obsect
c = pywebui.Connector('http://10.11.108.21:8082')
# Authenticate
c.login('testuser', 'testuser')
# Retrieve list of users
c.get_users()
```