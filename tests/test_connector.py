import pywebui

# def test_constructor():
#     c = pywebui.Connector('http://10.11.108.21:8082')
#
# def test_auth():
#     c = pywebui.Connector('http://10.11.108.21:8082')
#     c.login('testuser', 'testuser')

# def test_get_users_list():
#     c = pywebui.Connector('http://10.11.108.21:8082')
#     c.login('testuser', 'testuser')
#     print(c.get_users())

def test_get_user_detail():
    c = pywebui.Connector('http://10.11.108.21:8082')
    c.login('testuser', 'testuser')
    print(c.get_user('testuser'))