#!/usr/bin/env python

from distutils.core import setup

setup(name='pymocha',
      version='1.0',
      description='project to study python testing, mock an CI',
      author='Felipe Besson',
      author_email='flpbesson@gmail.com',
      url='http://www.fbesson.wordpress.com',
      packages=['pymocha'],
      install_requires=['httplib']
      )