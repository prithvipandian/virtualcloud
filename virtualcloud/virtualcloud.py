#!/usr/bin/python
import sys
from virtualcloud import db_ops



if len(sys.argv) == 1:
    VirtualCloudShell().cmdloop()

options = {
           'login' : db_ops.login,
           'upload' : db_ops.upload,
           'download' : db_ops.download
           'logout' : db_ops.logout
           }
           
options[argv[1]](argv[2:])


