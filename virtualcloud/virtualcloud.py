#!/usr/bin/python
import sys, virtualcloud



if len(sys.argv) == 1:
    VirtualCloudShell().cmdloop()

options = {
           'login' : virtualcloud.login,
           'upload' : virtualcloud.upload,
           'download' : virtualcloud.download
           'logout' : virtualcloud.logout
           }
           
options[argv[1]](argv[2:])


