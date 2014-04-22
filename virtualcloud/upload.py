#!/usr/bin/python

#Virtual Cloud 
#Manages uploading files to each service

import sys
import getopt
import tempfile
import hashlib
import db_ops
import json
import os

# Makes sure setup was run
def verifyLogin():
    # Loads the user information 
    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
            authkey = json.dumps(userclouds)
            return userclouds
    except IOError:
        print "Please login first!"
        sys.exit()


# Uploads an entire file to a certain service
# fileName: the full path of the file to be uploaded
# service: the name of the service to upload to
def uploadNotChunked(fileName, service):
    userclouds = verifyLogin()

    if (service == 'dropbox'):
        #Create new instance of Dropbox Operations
        db = db_ops.db(userclouds['dropbox'][0])
        #Upload File
        db.db_upload(fileName)
        print "File uploaded!"
        
    elif (service == 'drive'):
        print "Choosing Drive"
        gd = gd_ops.gd()
        gd.gd_upload(fileName)
        print "File uploaded!"

# Uploads a file in multiple chunks
# fn: the full path of the file to upload
# cs: chunksize in bytes
def upload(fn, cs):
    inputfile = ''
    chunksize = 0
    buffer = 1024

    filename = fn
    chunksize = int(cs)
    
    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
    except IOError:
        print "Please add an account first!"
        sys.exit()
    db_tokens = userclouds["dropbox"]
    dbclients = []
    for token in db_tokens:
        dbclients.append(db_ops.db(token))
        
    gd_tokens = userclouds["gdrive"]
    gdclients = []    
    for token in gd_tokens:
        gdclients.append(gd_ops.gd(token))

    prefix = hashlib.sha224(os.path.basename(filename)).hexdigest()
    
    with open (filename, 'r+b') as src:
        suffix = 0
        upload_completed = False
        while upload_completed is False:
            with tempfile.TemporaryFile() as target:
                data = src.read(chunksize)
                if data:
                    target.write(data)
                    #Iteration through clients TODO, temporarily only looks at first db client
                    outputfilepath = prefix + '.%s' % suffix
                    target.seek(0)
                    dbclients[0].db_upload(outputfilepath, target)
                    print "Uploaded piece: " + str(suffix)
                    suffix +=1
                else:
                    upload_completed = True
                    print "Upload Complete!"
                
if __name__ == "__upload__":
   upload(sys.argv[1:])
