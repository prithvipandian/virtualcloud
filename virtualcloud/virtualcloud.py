#!/usr/bin/python
import sys
import virtualcloudshell 
import db_ops


if len(sys.argv) == 1:
    virtualcloudshell.VirtualCloudShell().cmdloop()

options = {
           'login' : login,
           'upload' :upload,
           'download' : download,
           'logout' : logout
           }
           
options[argv[1]](argv[2:])


