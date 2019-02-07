#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Username',
      version='1.0',
      description='Search Usernames online',
      author='Ben P. Dorsi-Todaro',
      author_email='ben@bigbenshosting.com',
      license='GPL 3',
      classifiers=['Python3.7','Python 3.6'],
      platform='Linux',
      url='https://linuxphreak.github.io/username/',
      packages=find_packages(),
      install_requires=['requests','os','bs4']
     )