#!/usr/bin/env python

from setuptools import setup

with open('README.md') as file:
      readme = file.read()

with open('LICENSE') as file:
      license = file.read()

setup(name='samanage3',
      version='1.0',
      description='Library to interface with samanage',
      long_description=readme,
      author='Chris DiTusa (original author: John Bond)',
      author_email='cditusa@gmail.com',
      url='https://github.com/toose11/samanage',
      license=license,
      packages=['samanage'],
     )
