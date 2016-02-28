#!/usr/bin/env python3
from setuptools import setup, find_packages
import os
here = os.path.abspath(os.path.dirname(__file__))
#os.path.join("/".join(here.split("/")[:-1]),""),
with open("README.rst","r") as f:
	long_description = f.read()

setup(name='yad',
	version='0.9.11',
	description='A python interface for the Yad program',
	author='Sagar D V',
	author_email='dvenkatsagar@gmail.com',
	maintainer='Sagar D V',
	maintainer_email='dvenkatsagar@gmail.com',
	url='https://gitlab.com/dvenkatsagar/python-yad/',
	download_url='https://gitlab.com/dvenkatsagar/python-yad/repository/archive.zip',
	license='GPL3',
	long_description=long_description,
	include_package_data=True,
	classifiers=[
	"Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Natural Language :: English",
    "Operating System :: MacOS",
    "Operating System :: POSIX",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
	],
	install_requires=['pexpect>=3.3'],
	scripts=["gdie"],
	py_modules=["yad"]
	)
