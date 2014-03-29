#!/usr/bin/python

#Class to handle creating folder
#TODO: Make work with services besides dropbox

import dropbox
import json

# Asks the user for the name of the directory they want to create
def getName():
    dirName = raw_input("Enter the name of the folder you'd like to create: ")
    return dirName

# Only works with dropbox so far
def mkdir(dirName):

    #Loads the user information 
    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
    except IOError:
        print "Please login first!"
        sys.exit()

    db_tokens = userclouds["dropbox"]

    #Uses Dropbox API to create folder
    try:
        #Hard coded client key. BAD! How do I fetch from JSON?
        dropbox.client.DropboxClient("YaiET0Jc82AAAAAAAAAAARAcR7-gfebqxbP4Zl32D_THrwRf_0DSjA6QECqfLOcy", locale=None, rest_client=None).file_create_folder(dirName)
        print "Folder created!"
        
    # If the folder cannot be created raises exception
    except dropbox.rest.ErrorResponse:
        print "Folder not created"
        raise

    



