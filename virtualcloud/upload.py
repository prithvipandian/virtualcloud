#!/usr/bin/python

import sys
import getopt
import tempfile
import hashlib
import db_ops
import json

def upload(fn, cs):
    inputfile = ''
    chunksize = 0
    buffer = 1024

    filename = fn
    chunksize = cs
    
    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
    except IOError:
        print "Please login first!"
        sys.exit()
    db_tokens = userclouds["dropbox"]
    dbclients = []
    for token in db_tokens:
        dbclients.append(db_ops.db(token))
        
    gd_tokens = userclouds["gdrive"]
    gdclients = []    
    for token in gd_tokens:
        gdclients.append(gd_ops.gd(token))

    print(filename)
    prefix = hashlib.sha224(filename).hexdigest()
    
    with open (filename, 'r+b') as src:
        suffix = 0
        upload_completed = False
        while upload_completed is False:
            with tempfile.TemporaryFile() as target:
                written = 0
                while written <= chunksize:
                    data = src.read(buffer)
                    if data:
                        target.write(data)
                        written += buffer
                    else:
                        upload_completed = True
                #Iteration through clients TODO, temporarily only looks at first db client
                outputfilepath = prefix + '.%s' % suffix
                dbclients[0].db_upload(outputfilepath, target)
                suffix +=1


                
if __name__ == "__upload__":
   upload(sys.argv[1:])
