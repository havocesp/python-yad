Python Yad project
==================

python-yad is interface to yad for python. Inspired by the PyZenity Project.

YAD is a program that will display GTK+ dialogs, and return (either in the return code, or on standard output) the users input.
This allows you to present information, and ask for information from the user, from all manner of shell scripts.
YAD is the fork of Zenity program.


**YAD source page**:	http://sourceforge.net/projects/yad-dialog/


The API is very simple which has a main class known as YAD.

Example:

>>> from yad import YAD
>>> yad = YAD()
>>> yad.Calendar()

You can even check out the test application 'gdie'(Gnome-desktop-item-editor) in the terminal.

>>> gdie

Requirements
============
- Python 3.2 and above
- pexpect module
- yad program

Installation
============
Can be installed by using pip:

>>> sudo python3 -m pip install yad

or by manual installation:

>>> git clone https://gitlab.com/dvenkatsagar/python-yad.git
>>> cd python-yad/python-yad
>>> python3 setup.py build
>>> python3 setup.py install

Contact Us
==========
If you guys encounter any bugs, or issues. please contact me via email:

:Authors: Sagar D V <dvenkatsagar@gmail.com>
