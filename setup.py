#!/usr/bin/env python3
from setuptools import setup, find_packages
import os
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,"README.rst"),"r",encoding='utf-8') as f:
	long_description = f.read()

setup(name='yad',
	version='0.9.0',
	description='A python interface for the Yad program',
	author='Sagar D V',
	author_email='dvenkatsagar@gmail.com',
	maintainer='Sagar D V',
	maintainer_email='dvenkatsagar@gmail.com',
	url='https://bitbucket.org/dvenkatsagar/python-yad.git',
	download_url='https://dvenkatsagar@bitbucket.org/dvenkatsagar/python-yad/get/master.zip',
	license='MIT',
	long_description='\r\n'+long_description,
	 classifiers=[
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
	],
	install_requires=['pexpect>=3.3','imghdr','re','signal','tempfile'],
	py_modules=["yad"])
