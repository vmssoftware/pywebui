from pywebui import urls
from pywebui.exceptions import ConnectorException
from pywebui.response import ResponseObject


class Package(ResponseObject):
    def __repr__(self):
        return f'{self.name}.{self.version}'


class PackageHistory(Package):
    pass


class InstalledPackagesMethods:
    def get_installed_packages(self):
        packages = []
        r = self.get(urls.API_GET_INSTALLED_PACKAGES)
        if r.status_code == 200:
            for attrs in r.json():
                packages.append(Package(attrs))

        return packages

    def get_package_history(self, product):
        history = []
        r = self.get(urls.API_GET_INSTALLED_PACKAGE_HISTORY, product=product)
        if r.status_code == 200:
            for attrs in r.json():
                history.append(PackageHistory(attrs))
        elif r.status_code == 404:
            pass

        return history

    def export_package_history(self, product):
        r = self.get(urls.API_EXPORT_INSTALLED_PACKAGE_HISTORY, product=product)

        if r.status_code == 200:
            return r.text
        else:
            message = r.json()
            raise ConnectorException(message['details'])

    def delete_package(self, product): pass