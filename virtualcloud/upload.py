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
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
           print 'test.py -i <inputfile> -o <outputfile>'
           sys.exit()
        elif opt == '-d':
        elif opt == '-g':
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


    
if __name__ == "__main__":
   main(sys.argv[1:])
