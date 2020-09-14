from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Identifier(ResponseObject):
    IDENTIFIER_TYPE = 'IDENTIFIER'
    GID_TYPE = 'GID'

    TYPES = [IDENTIFIER_TYPE, GID_TYPE]

    ATTRIBUTES = [
        'RESOURCE',
        'DYNAMIC',
        'NOACCESS',
        'SUBSYSTEM',
        'HOLDER_HIDDEN',
        'NAME_HIDDEN'
    ]

    def __repr__(self):
        return f'{self.name}={self.value}'


class Holder(ResponseObject):
    def __repr__(self):
        return f'{self.holder}'


class IdentifiersMethods:
    def get_identifiers(self):
        identifiers = []
        r = self.get(urls.API_GET_IDENTIFIERS)
        if r.status_code == 200:
            for attrs in r.json():
                identifiers.append(Identifier(attrs))

        return identifiers

    def get_all_identifiers(self):
        identifiers = []
        r = self.get(urls.API_GET_ALL_IDENTIFIERS)
        if r.status_code == 200:
            for attrs in r.json():
                identifiers.append(Identifier(attrs))

        return identifiers

    def get_identifier(self, identifier):
        identifiers = self.get_all_identifiers()
        identifiers = list(filter(lambda i: i.name == identifier, identifiers))
        if identifiers:
            return identifiers[0]

    def get_identifier_holders(self, identifier):
        holders = []
        r = self.get(urls.API_GET_IDENTIFIER_HOLDERS, identifier=identifier)
        if r.status_code == 200:
            for attrs in r.json():
                holders.append(Holder(attrs))

        return holders

    def get_holder_identifiers(self, holder):
        identifiers = []
        r = self.get(urls.API_GET_HOLDER_IDENTIFIERS, holder=holder)
        if r.status_code == 200:
            data = r.json()
            if 'details' in data:
                return []
            for attrs in data:
                identifiers.append(Identifier(attrs))

        return identifiers

    def create_identifier(self, name, value, identifier_type=Identifier.IDENTIFIER_TYPE, attributes=[]):
        data = {
            "identName": name,
            "identValue":
                {
                    "value": value,
                    "type": identifier_type
                },
            "identAttrs": attributes
        }
        r = self.post(urls.API_CREATE_IDENTIFIER, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_identifier(self, identifier):
        r = self.delete(urls.API_DELETE_IDENTIFIER, identifier=identifier)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def grant_identifiers(self, username, identifiers):
        data = [{
            "username": username,
            "identifiers": identifiers
        }]
        r = self.put(urls.API_GRANT_IDENTIFIERS, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def rovoke_identifiers(self, username, identifiers):
        data = [{
            "username": username,
            "identifiers": identifiers
        }]
        r = self.put(urls.API_REVOKE_IDENTIFIERS, json=data)
        if r.status_code == 200:
            return True
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])
