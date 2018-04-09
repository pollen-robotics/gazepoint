#!/usr/bin/env python

import imp

from setuptools import setup, find_packages

version = imp.load_source('gazepoint.version', 'gazepoint/version.py')


setup(name='gazepoint',
      version=version.version,
      packages=find_packages(),
      install_requires=['lxml',
                        ],      
      )
