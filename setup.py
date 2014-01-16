#!/usr/bin/env python
import os
import sys

# import utilities version etc
from redis_utils import __version__

# import setuptools as needed
try:
	from setuptools import setup
	from setuptools.command.test import test as TestCommand
	
except ImportError:

	from distutils.core import setup

# grab our readme generated rst for this project
with open("readme.rst", "r") as f:

	long_description = f.read()

# grab installation dependencies
with open("requirements.txt", "r") as f:

	installation_requirements = f.read().splitlines()

# grab test requirements
with open("test-requirements.txt", "r") as f:

	test_requirements = f.read().splitlines()

print test_requirements

# setup project 
setup(
	name="redis-utils",
	version = __version__,
	description = "Redis utilities for TDD/BDD",
	long_description = long_description,
	url = "http://github.com/jonmorehouse/py-redis-utils",
	author = "Jon Morehouse",
	author_email = "morehousej09@gmail.com",
	keywords = ["redis", "utilities"],
	license = "MIT",
	packages = ["redis_utils"],
	include_package_data = True,
	install_requires = installation_requirements,
	tests_require = test_requirements,
	test_suite = "nose.collector",

	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.5',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
	]
)