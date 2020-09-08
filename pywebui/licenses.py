from urllib.parse import urljoin

from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class License(ResponseObject):
    def __repr__(self):
        return f'{self.productName}.{self.authorization}'


class LicenseHistory(License):
    def __repr__(self):
        return f'{self.productName}.{self.authorization}'


class LicenseMethods:
    def get_all_licenses(self):
        licenses = []
        r = self.get(urls.API_GET_ALL_LICENSES_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                licenses.append(License(attrs))

        return licenses

    def get_active_licenses(self):
        licenses = []
        r = self.get(urls.API_GET_ACTIVE_LICENSES_LIST)
        if r.status_code == 200:
            for attrs in r.json():
                licenses.append(License(attrs))

        return licenses

    def get_license(self, product, authorization):
        r = self.get(urls.API_GET_LICENSE, product=product, authorization=authorization)
        if r.status_code == 200:
            return License(r.json())
        elif r.status_code == 404:
            message = r.json()
            raise ConnectorException(message['details'])

    def get_license_history(self, product, authorization):
        history = []
        r = self.get(urls.API_GET_LICENSE_HISTORY, product=product, authorization=authorization)
        if r.status_code == 200:
            for attrs in r.json():
                history.append(LicenseHistory(attrs))
        elif r.status_code == 404:
            pass

        return history

    def register_license(self, product, data):
        r = self.post(urls.API_REGISTER_LICENSE, product=product, json=data)
        if r.status_code == 200:
            return License(r.json())
        elif r.status_code == 400:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_license(self, product, authorization):
        r = self.delete(urls.API_DELETE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_license_history(self, product, authorization):
        r = self.delete(urls.API_DELETE_LICENSE_HISTORY, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def export_license_history(self, product, authorization):
        r = self.get(urls.API_EXPORT_LICENSE_HISTORY, product=product, authorization=authorization)

        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def enable_license(self, product, authorization):
        r = self.put(urls.API_ENABLE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def disable_license(self, product, authorization):
        r = self.put(urls.API_DISABLE_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def load_license(self, product, authorization):
        r = self.post(urls.API_LOAD_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def unload_license(self, product, authorization):
        r = self.post(urls.API_UNLOAD_LICENSE, product=product, authorization=authorization)

        if r.status_code == 200:
            return True
        else:
            message = r.json()
            raise ConnectorException(message['details'])