import sys
import os
import getopt
import hashlib
import db_ops
import tempfile
import json

def download (filename, targetdir=os.getcwd()):
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

    prefix = hashlib.sha224(filename).hexdigest()

    #TODO: For now, only looking at dropbox client 0 
    dbfilelist = dbclients[0].client.metadata('/')['contents']
    infiles = []
    for file_data in dbfilelist:
        if file_data['is_dir']:
            continue
        if prefix in file_data['path']:
            infiles.append(file_data)

    infiles.sort(key = lambda k: int(k['path'].partition('.')[2]))       
    outfile = targetdir + '/' + filename
    
    with open(outfile, 'w+b') as target:
        for infile in infiles:
            with dbclients[0].db_download(infile['path']) as src:
                data = src.read()
                if data:
                    target.write(data)
                else:
                    break


if __name__ == "__download__":
   downloadload(sys.argv[1:])
