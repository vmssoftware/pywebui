#!/usr/bin/env python

from setuptools import setup

setup(name='pywebui',
      version='0.1',
      description='Python bind for OpenVMS Administration Tool',
      author='VMS Software',
      author_email='info@vmssoftware.com',
      packages=['pywebui', 'pywebui.tcpip'],
      package_data={'pywebui.tcpip': ['*']},
      install_requires=['requests==2.22.0'],
      setup_requires=['requests==2.22.0']
)