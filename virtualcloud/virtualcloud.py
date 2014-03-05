#!/usr/bin/python
import sys, getopt, virtualcloud



if len(sys.argv) == 1:
    VirtualCloudShell().cmdloop()

options = {'setup' : virtualcloud.setup,
           'login' : virtualcloud.login,
           'upload' : virtualcloud.upload,
           'download' : virtualcloud.download
           }
           
options[argv[1]](argv[2:])


