#!/usr/bin/env python3
from setuptools import setup, find_packages
import os
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,"README.rst"),"r") as f:
	long_description = f.read()

setup(name='yad',
	version='0.9.3',
	description='A python interface for the Yad program',
	author='Sagar D V',
	author_email='dvenkatsagar@gmail.com',
	maintainer='Sagar D V',
	maintainer_email='dvenkatsagar@gmail.com',
	url='https://bitbucket.org/dvenkatsagar/python-yad.git',
	download_url='https://dvenkatsagar@bitbucket.org/dvenkatsagar/python-yad/get/master.zip',
	license='MIT',
	long_description=long_description,
	include_package_data=True,
	classifiers=[
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
	],
	install_requires=['pexpect>=3.3'],
	scripts=["gdie"],
	py_modules=["yad"])
