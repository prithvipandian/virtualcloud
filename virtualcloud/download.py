import sys
import os
import getopt
import hashlib
import virtualcloud
import tempfile

def main (argv)
    filename = ''
    infiles = []
    targetdir = os.getcwd()
    buffer = 1024
    #Parsing command line input
    try:
        opts, args = getopt.getopt(argv,"hf:t:",["file=", "target="])
    except getopt.GetoptError:
        print 'download -f <filename> '
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print 'download -f <filepath>'
           sys.exit()
        elif opt in ("-f", "--file"):
            filename = arg
        elif opt in ("-t", "--target"):
            targetdir = arg

    try:
        with '.virtualcloud' as userjson:
            userclouds = json.load(userjson)
    except IOError:
        print "Please login first!"
        sys.exit()
    db_tokens = userclouds[db]
    dbclients = []
    for token in db_tokens:
        dbclients.append(db_ops.db(token))
        
    gd_tokens = userclouds[gd]
    gdclients = []    
    for token in gd_tokens:
        gdclients.append(gd_ops.gd(token))

    prefix = hashlib.sha224(filename).hexdigest()

    #TODO: For now, only looking at dropbox client 0 
    dbfiles = dbclients[0].metadata('/')[contents]
    for file_data in dbfiles:
        if file_data['is_dir']:
            continue
        if prefix in file_data['path']:
            infiles.append(file_data['path'])

    outfile = targetdir + '/' + filename
    with open(outfile, 'w+b') as target:
        for infile in sorted(infiles):
            with open(dbclients[0].db_download(infile), 'r+b') as src:
                while True:
                    data = src.read(buffer)
                    if data:
                        target.write(data)
                    else:
                        break
