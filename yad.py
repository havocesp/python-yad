# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Name: yad.py
Author:   D V Sagar
Created: 1/1/2015

Copyright (c) 2013-2015 Sagar D V(dvenkatsagar@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from datetime import date
from subprocess import Popen, PIPE
from signal import signal, SIGPIPE, SIG_DFL
import os
import re
import sys
import imghdr
import random
import pexpect
import tempfile
__all__ = ['Calendar','Color','DND','Entry','Icon','File','Font','List','Progress','MultiProgress','Scale','Print','Notify','Form','TextInfo','Notebook']

__version__ = "0.9.1"

__doc__ = """python-yad is interface to yad for python. Inspired by the PyZenity Project.

YAD is a program that will display GTK+ dialogs, and return (either in the return code, or on standard output) the users input.
This allows you to present information, and ask for information from the user, from all manner of shell scripts.
YAD is the fork of Zenity program.

The API is very simple which has a main class known as YAD. Type help(pyyad.YAD) to see documentation of functions.

Example:
    from yad import YAD
    yad = YAD()
    yad.Calendar()

Each function takes optional kwargs parameters which allows the use of general yad parameters.
"""
signal(SIGPIPE,SIG_DFL)
class YAD:
    """The main class used as the interface to Yad."""
    def __init__(self,exefile='/usr/bin/yad',shell='/bin/bash'):
        """
        Attributes:
            yad (str) :	string representing the yad program.
            shell (str) : string representing the systems shell i.e bash,kshell,cshell.
            args (list|tuple, optional) : An array of arguments for yad. Format = ["--ARG=VALUE"]. check 'man yad' for available values.

        Note:
            General key word arguments of python-yad are:
                center (bool, optional) : Place window on center of screen
                print_xid (bool, optional) : Print X Window Id of a dialog window to the stderr.
                image_on_top (bool, optional) : Show image above main widget instead of left. This option is always on for print dialog.
                no_buttons (bool,optional): Don't show buttons.
                no_markup (bool, optional): Don't use pango markup in dialog's text.
                always_print_result (bool, optional) : Always print result.
                dialog_sep (bool, optional) : Show separator between dialog and buttons. Works only with gtk+-2.0.
                sticky (bool, optional) : Make window visible on all desktops.
                fixed (bool, optional) : Make window fixed width and height.
                mouse (bool, optional) : Place window under mouse position.
                on_top (bool, optional) : Place window over other windows.
            	undecorated (bool, optional) : Make window undecorated (remove title and window borders).
            	skip_taskbar (bool, optional) : Don't show window in taskbar and pager.
            	maximized (bool, optional) : Run dialog window maximized.
            	fullscreen (bool, optional) : Run dialog in fullscreen mode. This option may not work on all window managers.
            	selectable_labels (bool, optional) :  If set, user can select dialog's text and copy it to clipboard. This option also affects on label fields in form dialog.
            	window_icon (str, optional) : Set the window icon.
                timeout (int, optional) : Set the dialog timeout in seconds.
            	timeout_indicator (bool, optional) : Set the dialog timeout in seconds.
            	kill_parent (signal, optional) : Send SIGNAL to parent process. Default value of SIGNAL is a SIGTERM. SIGNAL may be specified by it's number or symbolic name with or without SIG prefix. See signal(7) for details about signals.
            	text_align (str, optional) : Set type of dialog text justification. TYPE may be left, right, center or fill.
            	buttons_layout (str, optional) : Set buttons layout type. Possible types are: spread, edge, start, end or center.  Default is end.
            	on_top (bool, optional) : Place window over other windows.
            	skip_taskbar (bool, optional) :  Don't show window in taskbar and pager.
            	image (str, optional) : Set the dialog image which appears on the left side of dialog. IMAGE might be file name or icon name from current icon theme.
                text(str, optional) : Set the dialog text.
                title (str, optional) : Set the dialog title.
                width (int, optional) : Set the dialog width.
                height (int, optional) : Set the dialog height.
                expander (str, optional) : Hide main widget with expander. TEXT is an optional argument with expander's label.
                borders (int, optional) : Set dialog window borders.
                fullscreen (bool, optional) : Run dialog in fullscreen mode. This option may not work on all window managers.
                geometry (str, optional) : Use standard X Window geometry notation for placing dialog.  When this option is used, width, height, mouse and center options are ignored.
                rest (str, optional) : Read extra arguments from given file instead of command line. Each line of a file treats as a single argument.
                button (str, optional) : Add  the dialog button. May be used multiply times. ID is an exit code or a command. BUTTON may be gtk stock item name for predefined buttons (like gtk-close or gtk-ok) or text in a form LABEL[!ICON[!TOOLTIP]] where `!' is an item separator. Full list of stock items may be found in gtk-demo program, in snippet called "Stock Items and Icon Browser". If no buttons specified OK and Cancel buttons used. See EXIT STATUS section for more. If ID have a non-numeric value it treats like a command and click on such button doesn't close the dialog.
        """
        self.yad = str(exefile)
        self.shell = str(shell)

    # Calendar Dialog
    def Calendar(self,day=None,month=None,year=None,details=None,plug=False,**kwargs):
        """Prompt the user for a date.
        This will raise a Yad Calendar Dialog for the user to pick a date.

        Args:
            day (int, optional) : Day of pre-selected date.
            day (int, optional) : Day of pre-selected date.
            month (int, optional) :Month of pre-selected date.
            year (int, optional) : Year of pre-selected date.
            details (str, optional) : File with days details. Format = <date> <description>
                            date field is date in format, specified as '%m/%d/%Y'.
                            Description is a string with date details, which may include Pango markup.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            obj : datetime.date obj representing the date.

        Raises:
            TypeError,IOError

        Examples:
            >>> x = yad.Calendar(day=1,month=1,year=15)
            >>> print(x)
            2015-01-01
        """
        args = ["--calendar"]

        if day:
            try:args.append("--day=%d" % day)
            except TypeError: pass

        if month:
            try:args.append("--month=%d" % month)
            except TypeError: pass

        if year:
            try: args.append("--year=%d" % year)
            except TypeError: pass

        if details:
            try:
                os.stat(details)
                args.append("--details='%s'" % details)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid file for details.")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            month, day, year = [int(x) for x in re.split('[-,/]',retval)]
            return date(year, month, day)

    # Color Dialog
    def Color(self,color='#ffffff',extra=False,palette='/etc/X11/rgb.txt',plug=False,**kwargs):
        """Prompt the user to choose a color.
        This will raise a Yad Color Dialog for the user to pick a color.

        Args:
            color (str, optional) : Value for color. Should start with '#'.
            extra (bool, optional) : Display extra information.
            palette (str, optional) : File which has palette information
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str : A string representing the string

        Raises:
            ValueError,TypeError

        Examples:
            >>> x = yad.Color(color='#abcabc')
            >>> print(x)
            #abcabc
        """
        args = ["--color"]
        if color.startswith("#"):
            args.append("--init-color='%s'" % color)
        else:
            print("Warning: Invalid Color for 'init_color'")

        if extra: args.append("--extra")

        if palette:
            try:
                os.stat(palette)
                args.append("--palette='%s'" % palette)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid file for palette.")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            return retval

    # Drag and Drop Dialog
    def DND(self,cmd=None,tooltip=False,plug=False,**kwargs):
        """Prompt the user to drag and drop something.
        This will raise a Yad DND Dialog for the user.

        Args:
            cmd (str, optional)	: Executes as a command when something is dropped.
            tooltip (bool, optional) : Use the dialog text as tooltip.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str	: Filename or text or output of command that is dropped.

        Raises:
            TypeError

        Examples:
            >>> x = yad.DND(tooltip=True,text="Drag and Drop here")
        """
        args = ["--dnd"]
        if cmd: args.append("--command='%s'" % cmd)

        if tooltip: args.append("--tooltip")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            return retval


    # Text Entry Dialog
    def Entry(self,label=None,text=None,hide_text=False,use_completion=False,
    editable=False,numeric=None,licon=None,licon_action=None,ricon=None,
    ricon_action=None,data=[],plug=False,**kwargs):
        """Prompt the user to enter a value.
        This will raise a Yad Combo Box Entry Dialog for the user.

        Args:
            label (str, optional) : Entry label text.
            text (str, optional) : Entry text.
            hide_text (bool, optional) : Hide the entry text. Can then be used as passwords.
            use_completion (bool, optional) : Use completion.
            editable (bool, optional) : Make entries editable.
            numeric (list|tuple) : Array size 4. Format = [min,max,step,precision].
            licon (str, optional) : Icon displayed on the left of the entry
            licon_action (str, optional) : command to be executed when licon is clicked.
            ricon (str, optional) : icon displayed on the right of the entry
            ricon_action(str, optional) : command to be executed when ricon is clicked.
            data (list|tuple) : 1D array representing the entries of combo box
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str : Output of the text entered.

        Raises:
            TypeError, FileNotFoundError

        Examples:
            >>> x = yad.Entry(label="Pick a item",data=["apple","orange","banana"])

            >>> y = yad.Entry(label="Password",hide_text=True)

            >>> z = yad.Entry(label="pick an item or type one",data=["","apple","orange","banana"])
        """
        args = ["--entry"]
        if label: args.append("--entry-label='%s'" % label)

        if text: args.append("--entry-text='%s'" % text)

        if hide_text: args.append("--hide-text")

        if use_completion: args.append("--completion")

        if editable: args.append("--editable")

        if numeric:
            try: args.append("--numeric=[%d,%d,%d,%d]" % (numeric[0],numeric[1],numeric[2],numeric[3]))
            except TypeError: args.append("--numeric=[%d,%d,%d,%d]" % (0,65525,1,2))

        if licon:
            try:
                imghdr.what(licon)
                args.append("--licon='%s'" % licon)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid file for 'licon'")

        if licon_action: args.append("--licon-action='%s'" % licon_action)

        if ricon:
            try:
                imghdr.what(ricon)
                args.append("--ricon='%s'" % ricon)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid file for 'ricon'")

        if ricon_action: args.append("--ricon-action='%s'" % ricon_action)

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if data:
            try:
                for dat in data: args.append(str(dat))
            except IndexError:
                raise IndexError("Invalid data. 'data' must be 1D array representing the items of the Entry list.")

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            return retval

    # Icon Box Dialog
    def Icons(self,dir=None,use_generic=False,sort=False,descend=False,listen=False,
    item_width=256,compact=False,single_click=False,term=None,plug=False,**kwargs):
        """Shows a Icon Box which can also execute various command for each icon.

        Args:
            dir (str) : Folder to read icons from. It reads the .desktop files in the folder.
            use_generic (bool, optional) : Use GenericName instead of Name for shortcut label.
            sort_by_name (bool, optional) : Use field name instead of filename for sorting items.
            descend (bool, optional) : Sort items in descending order.
            listen (bool, optional) : Read from stdin. See `man yad` for more information.
            item_width (int, optional) : Set width of items.
            compact (bool, optional) : Use compact mode.
            single_click (bool, optional) : Allow single click to activate items.
            term (str, optional) : A pattern used for terminal. (default: 'xterm -e %s')
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            callback|returncode : callback function or return exit code for 'listen'
                                Args:
                                    name (str, optional) : name of icon to send
                                    tooltip (str, optional) : tooltip to display
                                    icon (str, optional) : icon to display
                                    cmd (str, optional) : command to execute when icon is clicked
                                    term (str, optional) : use terminal or not. see `man yad` for more info.
                                    ret (bool, optional) : get return retval or code

                                Returns:
                                    status : returncode of the proc

        Raises:
            TypeError, FileNotFoundError

        Examples:
            >>> x = yad.Icons("/usr/share/applications",compact=True)

            >>> x = yad.Icons(listen=True)
            >>> x(name="app1",tooltip="app1",icon=None,cmd="test.sh",term=True)
            >>> y = x(name="app2",tooltip="app2",icon=None,cmd="test.sh",term=True,ret=True)


            where test.sh:
                yad --text="Hello there, You have executed app1."

        """
        args = ["--icons"]
        if dir:
            try:
                os.stat(dir)
                args.append("--read-dir='%s'" % dir)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid Directory for 'dir'.")

        if use_generic: args.append("--generic")

        if sort: args.append("--sort-by-name")

        if descend: args.append("--descend")

        if listen: args.append("--listen")

        try: args.append("--item-width=%d" % item_width)
        except TypeError: args.append("--item-width=256")

        if compact: args.append("--compact")

        if single_click: args.append("--single-click")

        if term: args.append("--term='%s'" % term)

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        def update(name=None,tooltip=None,icon=None,cmd=None,term=False,ret=False):
            child.setecho(False)
            if name: child.sendline(name)
            else: child.sendline()

            if tooltip: child.sendline(tooltip)
            else: child.sendline()

            if icon:
                try:
                    imghdr.what(icon)
                    child.sendline(icon)
                except FileNotFoundError:
                    child.sendline()

            if cmd: child.sendline(cmd)
            else: child.sendline()

            if term: child.sendline("TRUE")
            else: child.sendline("FALSE")
            child.setecho(True)
            if ret:
                retval = child.read()
                child.close()
                rc = child.exitstatus
                return rc


        if listen:
            if plug: raise Exception("Error: 'plug' and 'listen' cannot be used together")
            cmd = " ".join([self.yad] + args)
            if sys.version_info[0] < 3:
                child = pexpect.spawn(cmd,timeout=None)
            else:
                child = pexpect.spawnu(cmd,timeout=None)
            return update
        else:
            if plug: return args
            retval,rc = self.execute(args=args)
            return rc


    # File Selection Dialog
    def File(self,filename=None,multi=False,dir=False,save=False,sep='|',
    preview=False,quoted=False,filters=None,**kwargs):
        """Shows a File Selection Dialog from which the user can choose a file.

        Args:
            filename (str, optional) : File to used as pre-selected option.
            multi (bool, optional) : Allows selection of multiple files.
            dir (bool, optional) : Allows only selection of directories.
            save (bool, optional) : Activate save mode.
            sep (str, optional) : character used as separator when returning multiple items.
            preview (bool, optional) : Add a preview widget to the file dialog.
            quoted (bool, optional) : Output values will be shell-style quoted.
            filters (list|tuple, optional) : Add a file filter. format ((NAME,PATTERN),(NAME,PATTERN),...).
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            list : List of filenames

        Raises:
            TypeError

        Examples:
            >>> x = yad.File(quoted=True,multi=True,preview=True)

            >>> x = yad.File(quoted=True,file_filters=(('py files','*.py'),('txt files','*.txt')))
        """
        if ('plug' or 'tabnum') in kwargs:
            raise IndexError("'plug' or 'tabnum' cannot be used with file dialog")

        args = ["--file"]
        if filename: args.append("--filename='%s'" % filename)

        if multi: args.append("--multiple")

        if dir: args.append("--directory")

        if save: args.append("--save")

        args.append("--separator='%s'" % sep)

        if preview: args.append("--add-preview")

        if quoted: args.append("--quoted-output")

        if filters:
            for filt in filters:
                try:
                    args.append("--file-filter='%s'|'%s'" % (filt[0],filt[1]))
                except TypeError:
                    print("Warning : Invalid 'filters'. It must be a multi-dimensional array in format ((NAME,PATTERN),(NAME,PATTERN),...)")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        retval,rc = self.execute(args=args)
        if rc == 0:
            regex = re.compile(r'[\n,\r,\t,\']')
            retval = regex.sub("",retval)
            return retval.split(sep)

    # Font Selection Dialog
    def Font(self,font=["Sans","Regular","12"],preview=None,plug=False,**kwargs):
        """Prompts the user to select a font.

        Args:
            font (list|tuple, optional) : 1D array representing the font. Format = ['Family-list','style-options','size'].
            preview (bool, optional) : Set preview text.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str : Font and size

        Raises:
            TypeError

        Examples:
            >>> x = yad.Font()
            >>> print(x)
        """
        args = ["--font"]
        try: args.append("--fontname='%s %s %s'" % (font[0],font[1],font[2]))
        except TypeError:
            print("Warning: Invalid font for 'font'. It should be an list of tuple in the format ['Family-list','style-options',size]")

        if preview: args.append("--preview='%s'" % preview)

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            return retval.split(' ')

    # List Dialog
    def List(self,colnames=[], boolstyle=None, sep='|',multi=False,
    editable=False, no_headers=False,no_click=False,print_all=False,
    print_col=0,hide_col=None, expand_col=0, search_col=0,limit=None,
    ellipsize=None, dclick_action=None,regex=None, listen=False,
    quoted=False, data=[],plug=False,**kwargs):
        """Shows a List Dialog box which allows the user to select an item.

        Args:
            colnames (list|tuple, optional) : 1D array of Names of all the columns in the Dialog
            boolstyle (bool, optional) : Should be either ["checklist","radiolist"]
            sep (str, optional) : Character used as separator when returning multiple items.
            multi (bool, optional) : Allow multiple item selection.
            editable (bool, optional) : Allow editing of items.
            no_headers (bool, optional) : Dont Show Column Headers
            no_click (bool, optional) : Disable sorting of column content by clicking on its header.
            print_all (bool, optional) : Print all data from the list.
            print_col (int, optional) : Print the specific column number. default = 0 (print all columns).
            hide_col (int, optional) : Hide specific column
            expand_col (int, optional) : Set the column expandable by default. default = 0 (sets all columns expandable).
            search_col (int, optional) : Set the quick search column. 0 mean to disable searching. By default search made on first column.
            limit (int, optional) : Set the number of rows in list dialog. Will be shown only the last NUMBER rows.
            ellipsize (str, optional) : Set ellipsize mode for text columns. Must be either ['NONE','START','MIDDLE','END'].
            dclick_action (str, optional) : Set the CMD as a double-click command. See `man yad` for more information.
            regex (str, optional) : Use regular expressions in search for text fields.
            listen (bool, optional) : Read from stdin. See `man yad` for more information.
            quoted (bool, optional) : Output values will be shell-style quoted.
            data (list|tuple, optional) : Multi-dimensional array. The size of the row's array must be equal to the number of columns.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            list|callback : List of items or a callback function for 'listen'
                                Args:
                                    data (list|tuple, optional) : Multi-Dimensional list or tuple of items to be passed

                                Returns:
                                    list : returns the list of items selected.

        Raises:
            TypeError,IndexError

        Examples:
            >>> x = yad.List(colnames=("No","item","Description"),quoted=True,data=(("1","apple","An apple"),("2","orange","An orange")))
            >>> print(x)

        """
        args = ["--list"]
        for col in colnames: args.append("--column='%s'" % col)

        if boolstyle:
            if boolstyle in ['checklist','radiolist']:
                args.append('--%s' % boolstyle)
            else:
                raise ValueError("'bool_style' should be of either these values ['checklist','radiolist']")

        args.append("--separator='%s'" % sep)

        if multi: args.append('--multiple')

        if editable: args.append('--editable')

        if no_headers: args.append('--no-headers')

        if no_click: args.append('--no-click')

        if print_all: args.append('--print-all')

        try:
            if print_col:
                args.append('--print-column=%d' % print_col)
        except TypeError:pass
        try:
            if hide_col:
                args.append('--hide-column=%d' % hide_col)
        except TypeError:pass
        try:
            if expand_col:
                args.append('--expand-column=%d' % expand_col)
        except TypeError:pass
        try:
            if limit:
                args.append('--limit=%d' % limit)
        except TypeError:pass

        if ellipsize:
            if not ellipsize in ["START","MIDDLE","END"]:
                args.append("--ellipsize='%s'" % ellipsize)
            else:
                raise ValueError("'ellipsize' must be either START,MIDDLE,END")

        if dclick_action: args.append("--dclick-action='%s'" % dclick_action)

        if regex: args.append("--regex-search='%s'" % regex)

        if listen: args.append('--listen')

        if quoted: args.append('--quoted-output')

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if data:
            for dat in data:
                for i in range(0,len(colnames)-len(dat)):
                    dat.append('')
                for d in dat:
                    args.append("'%s'" % d)

        def update(data=[],ret=False):
            child.setecho(False)
            if data:
                for dat in data:
                    for i in range(0,len(colnames)-len(dat)):
                        dat.append('')
                    for d in dat:
                        child.sendline("%s" % d)
            child.setecho(True)
            if ret:
                retval = child.read()
                regex = re.compile(r'[\n,\r,\t,\']')
                retval = regex.sub("",retval)
                retval = retval.rstrip(sep).split(sep)
                child.close()
                rc = child.exitstatus
                if rc == 0:
                    return retval

        if listen:
            if plug: raise Exception("Error: 'plug' and 'listen' cannot be used together")
            cmd = " ".join([self.yad] + args)
            if sys.version_info[0] < 3:
                child = pexpect.spawn(cmd,timeout=None)
            else:
                child = pexpect.spawnu(cmd,timeout=None)
            return update
        else:
            if plug: return args
            retval,rc = self.execute(args=args)
            if rc == 0:
                regex = re.compile(r'[\n,\r,\t,\']')
                retval = regex.sub("",retval)
                retval = retval.rstrip(sep).split(sep)
                return retval

    # Notification Dialog
    def Notify(self,cmd=None,listen=False,sep='|',item_sep='!',menu=[],
    no_middle=False,hidden=False,icon=None,text=None,**kwargs):
        """Sets a Notification icon in the message tray.

        Args:
            cmd (str, optional) : Set the command running when clicked on the icon. Default action is quit if --listen not specified.
            listen (bool, optional) : Read from stdin. See `man yad` for more information.
            sep (str, optional) : Character used as separator when returning multiple items.
            item_sep (str, optional) : Character used as separator when returning multiple sub-items.
            menu (list|tuple, optional) : Multi-dimensional array representing the items of the indicator menu. Format = ((NAME,ACTION,ICON),(NAME,ACTION,ICON),...).
            no_middle (bool, optional) : Disable exit on middle click.
            hidden (bool, optional) : Dont show icon at startup.
            icon (str, optional) : Icon for the indicator.
            text (str, optional) : Tooltip text to be shown when user hovers on indicator.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str|callback : returns a string of the output of the command executed in the notification or a callback function for 'listen'.
                                Args:
                                    icon (str, optional) : icon to display or update
                                    tooltip (str, optional) : tooltip to display
                                    visible (str, optional) : make icon visible or not. Options are "true","false","blink"
                                    action (str, optional) : change command to execute
                                    menu (list|tuple, optional) : Multi-dimensional list or tuple representing the menu items of the notification
                                    q (bool, optional) : whether to quit or not
                                    ret (bool, optional) : whether to get return value or not

                                Return:
                                    str : output of the commands executed

        Raises:
            IndexError, FileNotFoundError

        Examples:
            >>> yad.Notify(cmd="nautilus",menu=(("nautilus","nautilus",""),("evince","evince"),("quit","quit","")))
        """
        if ('plug' or 'tabnum') in kwargs:
            raise IndexError("'plug' or 'tabnum' cannot be used with Notification dialog")

        args = ["--notification"]
        if cmd: args.append("--command='%s'" % cmd)

        if listen: args.append("--listen")

        args.append("--separator='%s'" % sep)

        args.append("--item-separator='%s'" % item_sep)

        if menu:
            try :
                menu_string = sep.join([item_sep.join(m) for m in menu])
                args.append("--menu='%s'" % menu_string)
            except IndexError:
                raise IndexError("Invalid format of 'menu'. Format should be ((NAME,ACTION,ICON),(NAME,ACTION,ICON),...)")

        if no_middle: args.append("--no-middle")

        if hidden: args.append("--hidden")

        if icon:
            try:
                imghdr.what(icon)
                args.append("--window-icon='%s'" % icon)
            except FileNotFoundError:
                raise FileNotFoundError("Invalid file for 'icon'")

        if text: args.append("--text='%s'" % text)

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        def update(icon=None,tooltip=None,visible="true",action=None,menu=[],q=False,ret=False):
            child.setecho(False)
            if icon:
                try:
                    imghdr.what(icon)
                    child.sendline("icon:'%s'" % icon)
                except FileNotFoundError:
                    pass

            if tooltip: child.sendline("tooltip:'%s'" % tooltip)

            if visible in ["true","false","blink"]: child.sendline("visible:%s" % visible)

            if action: child.sendline("action:%s" % action)

            if menu:
                try :
                    menu_string = sep.join([item_sep.join(m) for m in menu])
                    child.sendline("menu:%s" % menu_string)
                except IndexError:
                    pass

            if q: child.sendline("quit")
            child.setecho(True)
            if ret:
                retval = child.read()
                child.close()
                rc = child.exitstatus
                if rc == 0:
                    return retval

        if listen:
            cmd = " ".join([self.yad] + args)
            if sys.version_info[0] < 3:
                child = pexpect.spawn(cmd,timeout=None)
            else:
                child = pexpect.spawnu(cmd,timeout=None)
            return update
        else:
            retval,rc = self.execute(args=args)
            if rc == 0:
                return retval

    # Print Dialog
    def Print(self,filename,type=None,headers=False,preview=False,font=None,**kwargs):
        """Shows a print dialog box.

        Args:
            filename (str) : file to print.
            type (str, optional) : type of file. Must either be TEXT,IMAGE,RAW.
            headers (bool, optional) : Add headers to the top of page with filename and page number. This option doesn't work for RAW type.
            preview (bool, optional) : Add Preview button to the print dialog. This option doesn't work for RAW type.
            font (list|tuple, optional) : 1D array representing the font. Format = ['Family-list','style-options','size'].
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            bool : True

        Raises:
            TypeError,ValueError,FileNotFoundError

        Examples:
            >>> yad.Print("test.pdf")
        """
        if ('plug' or 'tabnum') in kwargs:
            raise IndexError("'plug' or 'tabnum' cannot be used with file dialog")

        args = ["--print"]
        try:
            os.stat(filename)
            args.append("--filename='%s'" % filename)
        except FileNotFoundException:
            print("Warning: Invalid file for 'filename'")

        if type:
            if type in ["TEXT","IMAGE","RAW"]:
                args.append("--type=%s" % type)
            else:
                raise ValueError("'type' must be either TEXT,IMAGE,RAW.")

        if headers: args.append("--headers")

        if preview: args.append("--add-preview")

        if font:
            try: args.append("--fontname='%s %s %s'" % (font[0],font[1],font[2]))
            except TypeError:
                print("'font' should be an list of tuple in the format ['Family-list','style-options','size']")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        retval,rc = self.execute(args=args)
        if rc == 0:
            return retval

    # Text Info Dialog
    def TextInfo(self,filename=None,editable=False,fore="#000000",back="#ffffff",font=["Sans","Regular","12"],wrap=False,
    justify="left",margins=0,tail=False,show_uri=False,listen=False,plug=False,**kwargs):
        """Show the text of a file to the user.

        This will raise a Yad Text Information Dialog presenting the user with
        the contents of a file.  It returns the contents of the text box.

        Args:
            filename (str) : file to read from.
            editable (bool, optional) : Allow changes to text.
            fore (str, optional) : Color to use as foreground color.
            back (str, optional) : Color to use as background color.
            font (list|tuple, optional) : 1D array representing the font. Format = ['Family-list','style-options','size'].
            wrap (bool, optional) : Enable text wrapping.
            justify (str, optional) : Set justification. TYPE may be left, right, center or fill.  Default is left.
            margins (int, optional) : Set text margins to SIZE.
            tail (bool, optional) : Autoscroll to end when new text appears. Works only when text is read from stdin.
            show_uri (bool, optional) : Make URI in text clickable. Links opens with xdg-open command.
            listen (bool, optional) : Read from stdin. See `man yad` for more information.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            str|callback : Contents of text box or callback function for 'listen'
                                Args:
                                    s (str, optional) : string to display in the textbox

                                Returns:
                                    str|returncode : either returns content of the box or return code depending on the parameters given to the main process

        Raises:
            TypeError

        Examples:
            >>> x = yad.TextInfo("test.txt",editable=True,wrap=True,justify="fill",tail=True)
            >>> print(x)
        """
        args = ["--text-info"]
        if filename:
            try:
                os.stat(filename)
                args.append("--filename='%s'" % filename)
            except FileNotFoundError:
                print("Warning: Invalid file for 'filename'.Enabling listen mode.")
                if not listen:
                    args.append("--listen")

        if editable: args.append("--editable")

        if fore.startswith("#"):
            args.append("--fore='%s'" % fore)
        else:
            print("Warning:Color cannot be identified. Please use the appropriate color format.")

        if back.startswith("#"):
            args.append("--back='%s'" % back)
        else:
            print("Warning:Color cannot be identified. Please use the appropriate color format.")

        if font:
            try: args.append("--fontname='%s %s %s'" % (font[0],font[1],font[2]))
            except TypeError:
                print("'font' should be an list of tuple in the format ['Family-list','style-options','size']")

        if wrap: args.append("--wrap")

        if justify in ["left","right","center","fill"]:
            args.append("--justify='%s'" % justify)
        else:
             print("Warning: 'justify' must either be left,right,center,fill.")

        try: args.append("--margins=%d" % margins)
        except TypeError: pass

        if tail: args.append("--tail")

        if show_uri: args.append("--show-uri")

        if listen: args.append("--listen")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        def update(s=None,ret=False):
            child.setecho(False)
            if s: child.sendline(s)
            child.setecho(True)
            if ret:
                retval = child.read()
                child.close()
                rc = child.exitstatus
                if rc == 0:
                    return retval.decode("utf8")
            else:
                child.wait()
                child.close()
                rc = child.exitstatus
                return rc

        if listen:
            if plug: raise Exception("Error: 'plug' and 'listen' cannot be used together.")
            cmd = " ".join([self.yad] + args)
            if sys.version_info[0] < 3:
                child = pexpect.spawn(cmd,timeout=None)
            else:
                child = pexpect.spawnu(cmd,timeout=None)
            return update
        else:
            if plug: return args
            retval,rc = self.execute(args=args)
            if rc == 0:
                return retval

    # Scale Dialog
    def Scale(self,value=0,min=0,max=65525,step=1,page=10,
    partial=False,hide=False,vertical=False,invert=False,
    mark=None,plug=False,**kwargs):
        """Shows a scale Dialog. allows the user to select value between a range.

        Args:
            value (int, optional) : Set initial value.
            min (int, optional) : Set minimum value.
            max (int, optional) : Set maximum value.
            step (int, optional) : Set step size.
            page (int, optional) : Set paging size. By default page value is STEP*10.
            partial (bool, optional) : Print partial values.
            hide (bool, optional) : Hide value.
            vertical (bool, optional) : Show vertical scale.
            invert (bool, optional) : Invert scale direction.
            mark (list|tuple, optional) : Add a mark to scale. Format = (('NAME',VALUE),('NAME',VALUE),...)
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            int : Returns a int

        Raises:
            TypeError

        Examples:
            >>> x = yad.Scale()
            >>> print(x)
        """
        args = ["--scale"]
        try:args.append("--value=%d" % value)
        except TypeError:pass
        try: args.append("--min-value=%d" % min)
        except TypeError:pass
        try: args.append("--max-value=%d" % max)
        except TypeError:pass
        try: args.append("--step=%d" % step)
        except TypeError:pass
        try: args.append("--page=%d" % page)
        except TypeError:args.append("--page=%d" % step*10)

        if partial: args.append("--print-partial")

        if hide: args.append("--hide-value")

        if vertical: args.append("--vertical")

        if invert: args.append("--invert")

        if mark:
            try:
                for m in mark: args.append("--mark=%s:%d" % (m[0],int(m[1])))
            except TypeError:
                print("Warning: 'mark' should be a multi-dimensional list or tuple of the format (('NAME',VALUE),('NAME',VALUE),...)")


        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            return int(retval)

    # Progress Dialog
    def Progress(self,text=None,percent=0,rtl=False,autoclose=False,
    autokill=False,pulsate=False,log=None,log_on_top=False,log_expanded=False,
    log_height=30,**kwargs):
        """Show a progress dialog to the user.

        Note:
            This function sends the SIGPIPE signal if the user hits the cancel button. You must connect to this signal if you do not want to get an error.

        Args:
            text (str, optional) : Set text in progress bar.
            percent (int, optional) : Set initial percentage.
            rtl (bool, optional) : Set Right-To-Left progress bar direction.
            autoclose (bool, optional) : Close dialog when 100% has been reached.
            autokill (bool, optional) : Kill parent process if cancel button is pressed.
            pulsate (bool, optional) : Pulsate progress bar.
            log (str, optional) : Show log window. This window gathers all of lines from stdin, started from # instead of setting appropriate progress labels.
            log_on_top (bool, optional) : Place log window above progress bar.
            log_expanded (bool, optional) : Start with expanded log window.
            log_height (int, optional) : Set the height of log window.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.


        Returns:
            callback : Returns a callback that accepts two arguments.
                                Args:
                                    percent (int|float):	set percentage of the bar.
                                    msg (str, optional):	message to be shown in the bar.

                                Returns:
                                    status:	returncode of the proc

        Raises:
            TypeError,BrokenPipeError

        Examples:
            >>> x = yad.Progress()
            >>> for i in range(0,100):
            ...	  x(i,msg=str(i)+" done")
            ...
            ...	  time.sleep(0.2)
        """
        if ('plug' or 'tabnum') in kwargs:
            raise IndexError("'plug' or 'tabnum' cannot be used with file dialog")

        args = ["--progress"]
        if text: args.append("--progress-text='%s'" % text)

        if percent:
            try:args.append("--percentage=%d" % percent)
            except TypeError: pass

        if rtl: args.append("--rtl")

        if autoclose: args.append("--auto-close")

        if autokill: args.append("--auto-kill")

        if pulsate: args.append("--pulsate")

        if log: args.append("--enable-log='%s'" % log)

        if log_on_top: args.append("--log-on-top")

        if log_expanded: args.append("--log-expanded")

        try: args.append("--log-height=%d" % log_height)
        except TypeError: pass

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        # Amazing way to handle updating it. Thanks Brian Ramos
        def update(percent,msg=''):
            """Call back function to update progress bar.

            Args:
                percent (int|float) : set percentage of the bar.
                msg (str, optional) : message to be shown in the bar.

            Returns:
                status : returncode of the proc
            """
            if type(percent) == float:
                percent = int(percent * 100)
            p.stdin.write('%d\n' % percent)
            if msg:
                p.stdin.write('# %s\n' % msg)
            return p.returncode

        p = Popen([self.yad] + args,stdin=PIPE,stdout=PIPE,universal_newlines=True)
        return update


    def MultiProgress(self,bar=[],vertical=False,align="left",autoclose=False,autokill=False,**kwargs):
        """Display multi progress bars dialog.

        Note:
            This function sends the SIGPIPE signal if the user hits the cancel button. You must connect to this signal if you do not want to get an error.

        Args:
            bar (list|tuple, optional) : Adds progress bar. A multi-dimensional array. Format = ((LABEL,TYPE),(LABEL,TYPE),...). LABEL is a text label for progress bar.
                                TYPE is a progress bar type. Types are: NORM for normal progress bar, RTL for inverted progress bar and PULSE for pulsate progress bar.
            vertical (bool, optional) : Set vertical orientation of progress bars.
            align (str, optional) : Set alignment of bar labels. Possible types are left, center or right. Default is left.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            callback : Returns a callback that accepts two arguments.
                                Args:
                                    percent (int|float): set percentage of the bar.
                                    bar (int): bar number to update
                                    msg (str, optional): message to be shown in the bar.

                                Returns:
                                    status:	returncode of the proc

        Raises:
            TypeError, BrokenPipeError

        Examples:
            >>> x = yad.MultiProgress(bar=(("bar1","NORM"),("bar2","PULSE")),autokill=True,autoclose=True)
            >>> for i in range(0,100):
            ...	  x(i,1,msg=str(i)+"% done")
            ...	  x(i,2,msg=str(i)+"% done")
            ...	  time.sleep(0.1)
            >>> x(100,1,msg="100% done")
            >>> x(100,2,msg="100% done")
        """
        if ('plug' or 'tabnum') in kwargs:
            raise IndexError("'plug' or 'tabnum' cannot be used with file dialog")

        args = ["--multi-progress"]
        for b in bar:
            if b[1] in ["NORM","RTL","PULSE"]:
                args.append("--bar=%s:%s" % (b[0],b[1]))
            else:
                print("Warning: The TYPE of 'bar' must be either NORM,RTL,PULSE")
                args.append("--bar=%s:NORM" % b[0])

        if vertical: args.append("--vertical")

        if align in ["left","right","center"]:
            args.append("--align=%s" % align)
        else:
            print("Warning: 'align' must either be left,right,or center.")

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s=%s" % generic_args)

        # Amazing way to handle updating it. Thanks Brian Ramos
        def update(percent,bar,msg=''):
            """Call back function to update progress bar.

            Args:
                percent (int|float) : set percentage of the bar.
                bar (int) : bar number to update
                msg (str, optional) : message to be shown in the bar.

            Returns:
                status : returncode of the proc
            """
            if type(percent) == float:
                percent = int(percent * 100)
            p.stdin.write("%d:%d\n" % (bar,percent))
            if msg:
                p.stdin.write('%d:# %s\n' % (bar,msg))
            return p.returncode

        p = Popen([self.yad] + args,stdin=PIPE,stdout=PIPE,universal_newlines=True)
        return update

    def Form(self,fields=[],align="left",cols=1,sep="|",item_sep="!",
    scroll=False,quoted=False,plug=False,**kwargs):
        """Shows a Form Dialog.

        Args:
            fields (list|tuple, optional) : Multi-dimensional array. see `man yad` for type of fields. Format = ((TYPE,LABEL,VALUE),(TYPE,LABEL,VALUE),...)
            align (str, optional) : Set alignment of bar labels. Possible types are left, center or right. Default is left.
            cols (int, optional) : Set number of columns in form. Fields will be placed from top to bottom.
            sep (str, optional) : Character used as separator when returning multiple items.
            item_sep (str, optional) : Character used as separator when returning multiple sub-items.
            scroll (bool, optional) : Make form scrollable.
            quoted (bool, optional) : Output values will be shell-style quoted.
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            dictionary : dictionary output of all fields

        Raises:
            IndexError, ValueError

        Examples:
            >>> x = (
            ... ("LBL","Well this is label"),
            ... ("","Default text entry","hello there"),
            ... ("H","Hidden label","Hidden text"),
            ... ("NUM","Numeric",(0,0,100,1,2)),
            ... ("CB","Combo box",("val1","^val2","val3")),
            ... ("CBE","Editable Combo box",("val1","^val2","val3")),
            ... ("FL","Select a file",""),
            ... ("SFL","File to save",""),
            ... ("DIR","Select Directory",""),
            ... ("CDIR","Create Directory",""),
            ... ("FN","Select Font",("Sans","Regular","12")),
            ... ("MFL","Select Multiple files",""),
            ... ("DT","Date",""),
            ... ("SCL","Scale",""),
            ... ("CLR","Color Palette",""),
            ... ("TXT","Multi-line text entry",""),
            ... ("CHK","Checkbox","true"),
            ... ("BTN",("gtk-ok","","OK"),"echo hi"),
            ... )
            >>> y = yad.Form(fields=x)
            >>> print(y)
        """
        def parser(f):
            args = []
            # Parse Field types
            if f[0] == "": args.append("--field='%s'" % f[1])
            else:
                if isinstance(f[1],str): args.append("--field='%s':%s" % (str(f[1]),f[0]))
                else: args.append("--field='%s':%s" % (item_sep.join([str(x) for x in f[1]]),f[0]))

            # Parse Data
            if f[0].upper() == "LBL": args.append("''")
            elif f[0].upper() == "NUM":
                try: args.append("'%s'" % (item_sep.join([str(i) for i in f[2][:2]])+".."+item_sep.join([str(i) for i in f[2][3:]])))
                except IndexError:
                    x = [0,0,65525,1,2]
                    args.append("'%s'" % (item_sep.joint([str(i) for i in x[:2]])+".."+item_sep.join([str(i) for i in x[3:]])))
            elif f[0].upper() == "CHK":
                if f[2].upper() in ["TRUE","FALSE"]:
                    args.append("'%s'" % f[2].upper())
                else:
                    args.append("'FALSE'")
            elif f[0].upper() in ["CB","CBE"]:
                args.append("'%s'" % item_sep.join([str(x) for x in f[2]]))
            elif f[0].upper() == "FN":
                args.append("'%s'" % " ".join([str(x) for x in f[2]]))
            else:
                # Fields that require direct values
                try:args.append("'%s'" % str(f[2]))
                except IndexError:pass

            return args

        args = ["--form"]

        if align in ["left","right","center"]:
            args.append("--align='%s'" % align)
        else:
            raise ValueError("'align' must either be left,right,or center.")

        try: args.append("--columns=%d" % cols)
        except TypeError: pass

        args.append("--separator='%s'" % sep)

        args.append("--item-separator='%s'" % item_sep)

        if scroll: args.append("--scroll")

        if quoted: args.append("--quoted-output")

        if fields:
            for field in fields:
                args += parser(field)

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if plug: return args
        retval,rc = self.execute(args=args)
        if rc == 0:
            retval = retval.splitlines()[-1].split(sep)
            dic = {}
            for i in range(len(fields)):
                dic[i] = retval.pop(0)
            return dic

    def Notebook(self,key=None,tabpos="top",border=None,tabs=[],**kwargs):
        """Shows up a Notebook Dialog. It is a special dialog that swallows other dialogs in it.
        It identifies the other dialogs with the 'plug' option and uses a unique randomly generated key to create the dialog.
        Please check example.

        Note:
            - It doesnt work if the other dialogs have 'listen' argument in it.

        Args:
            key (int) : A unique key used by notebook. It will automatically keep the plug value.
            tabpos (str, optional)  :   Set the tabs position. Value may be top, bottom, left, or right.
            border (int)  : Set the tabs position. Value may be top, bottom, left, or right.
            tabs (list|tuple) : A multi-dimensional list or tuple which represents the tab. Format = ((TABNAME,ARGS),(TABNAME,ARGS),...)

        Returns:
            dictionary : outputs of all the tags

        Examples:
            >>> x = yad.execute(plug=True,text="This is tab1 text")
            >>> y = yad.execute(plug=True,text="This is tab2 text")
            >>> z = yad.Calendar(plug=True,text="This is a tab3 calendar")
            >>> tabs =(
            ... ("Tab1",x),
            ... ("Tab2",y),
            ... ("Tab3",z),
            ... )
            >>> tabdata = yad.Notebook(12345,tabpos='bottom',tabs=tabs)
            >>> print(tabdata)
        """
        args = ["--notebook"]
        if not key:
            key = random.randInt(10000,20000)
        args.append("--key=%d" % key)

        if tabpos in ["top","bottom","left","right"]:
            args.append("--tab-pos='%s'" % tabpos)

        if border:
            try: args.append("--tab-borders=%d" % border)
            except TypeError: pass

        arr = []
        tf = []
        for i,tab in enumerate(tabs):
            f = tempfile.NamedTemporaryFile()
            tf.append(f)
            args.append("--tab='%s'" % tab[0])
            x = [self.yad]
            x.append("--plug=%d" % key)
            x.append("--tabnum=%d" % (i+1))
            x += tab[2]
            x.append("&>")
            x.append(f.name)
            x.append("&")
            arr.append(" ".join(x))

        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if sys.version_info[0] < 3:
            child = pexpect.spawn(self.shell,timeout=None)
        else:
            child = pexpect.spawnu(self.shell,timeout=None)
        child.setecho(False)
        child.sendline("ipcrm -m %s" % key)
        for i in arr:
            child.sendline(i)
        child.setecho(True)
        retval,rc = self.execute(args=args)
        #child.close()
        if rc == 0:
            dic = {}
            for i,tab in enumerate(tabs):
                dic[i+1] = tf[i].read()
                tf[i].close()
            return dic

    # execute yad
    def execute(self,args=[],plug=False,**kwargs):
        """Exceutes yad using pexpect module.

        Args:
            args (list|tuple, optional) : yad arguments can be passed here directly. Format = "--ARG=VALUE"
            **kwargs : Optional command line parameters for Yad such as height,width,title etc.

        Returns:
            tuple : Returns the retval and returncode of the command executed

        Raises:
            TypeError

        Example:
            >>> yad = yad.YAD()
            >>> x = yad.execute(args=["--calendar","--day=15","--month=1","--year=2016"])
            >>> print(x)
        """
        for generic_args in self.kwargs_helper(kwargs):
            try: args.append("--%s" % generic_args)
            except TypeError: args.append("--%s='%s'" % generic_args)

        if any("--listen" in s for s in args) or "listen" in kwargs:
            if plug: raise Exception("Error: 'plug' and 'listen' cannot be used together")
        else:
            if plug: return args
        cmd = " ".join([self.yad] + args)
        if sys.version_info[0] < 3:
            retval,rc = pexpect.run(cmd,withexitstatus=True,timeout=None)
        else:
            retval,rc = pexpect.runu(cmd,withexitstatus=True,timeout=None)
        retval = retval.strip()
        return (retval,rc)

    # kwargs helper
    def kwargs_helper(self,kwargs):
        """This function preprocesses the kwargs dictionary to sanitize it."""
        args = []

        # These are boolean parameters that are passed in kwargs.
        generic_bool = ["center","print-xid","image-on-top",
        "no-buttons","no-markup","always-print-result",
        "dialog-sep","sticky","fixed",
        "mouse","on-top","undecorated",
        "skip-taskbar","maximized","fullscreen",
        "selectable-labels",'listen']

        # This is a dictionary of optional parameters that would create
        # syntax errors in python if they were passed in as kwargs.
        generic = {'window_icon': 'window-icon','timeout_indicator' : 'timeout-indicator',
        'kill_parent' : 'kill-parent','print_xid' : 'print-xid','text_align' : 'text-align',
        'no_buttons' : 'no-buttons','buttons_layout' : 'buttons-layout','no_markup' : 'no-markup',
        'always_print_result' : 'always-print-result','dialog_sep' : 'dialog-sep',
        'on_top' : 'on-top','skip_taskbar' : 'skip-taskbar', 'selectable_labels' : 'selectable-labels',
        'image_path' : 'image-path'}

        for param, value in kwargs.items():
            param = generic.get(param, param)
            if param in generic_bool:
                if value:
                    args.append((param))
            elif param.startswith("button"):
                args.append(("button",value))
            else:
                args.append((param, value))
        return args
