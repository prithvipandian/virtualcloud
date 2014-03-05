#!/usr/bin/python
import sys
import virtualcloud



if len(sys.argv) == 1:
    VirtualCloudShell().cmdloop()

options = {
           'login' : virtualcloud.db_ops.db_login,
           'upload' : virtualcloud.upload,
           'download' : virtualcloud.download,
           'logout' : virtualcloud.logout
           }
           
options[argv[1]](argv[2:])


