#!/usr/bin/python

import sys, getopt
import tempfile
import subprocess
import hashlib
import db_ops

divide_script = '''\

'''
def main(argv):
    inputfile = ''
    chunksize = 0;
    dropbox = false
    gdrive = false

    #Parsing command line input
    try:
        opts, args = getopt.getopt(argv,"hdgf:s:",["filename=","sizechunk="])
    except getopt.GetoptError:
        print 'upload -f <filepath> -s <chunksize> -d [for dropbox] -g [for gdrive]'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print 'upload -f <filepath> -s <chunksize> -d [for dropbox] -g [for gdrive]'
           sys.exit()
        elif opt == '-d':
            dropbox = true
        elif opt == '-g':
            gdrive = true
        elif opt in ("-f", "--file"):
            filename = arg
        elif opt in ("-s", "--sizechunk"):
            chunksize = int(opt)

    prefix = hashlib.sha224(filename).hexdigest()



    split_bash = "split -b" + chunksize + " " + inputfile + " " + prefix
    
    with tempfile.NamedTemporaryFile() as scriptfile:
        scriptfile.write(split_bash)
        scriptfile.flush()
        subprocess.call(['/bin/bash', scriptfile.name])
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

def split_file(file, prefix, max_size, buffer=1024):
    if dropbox:
        db = db_ops.db()
        
    with open (file, 'r+b') as src:
        suffix = 0
        while True:
            with tempfile.TemporaryFile() as target:
                written = 0
                while written <= max_size
                    data = src.read(buffer)
                    if data:
                        target.write(data)
                        written += buffer
                    else:
                        return suffix
                suffix +=1

                
open(prefix + '.%s' % suffix, 'w+b'
    
if __name__ == "__main__":
   main(sys.argv[1:])
