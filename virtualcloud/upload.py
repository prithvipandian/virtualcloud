#!/usr/bin/python

import sys
import getopt
import tempfile
import hashlib
import db_ops
import json
import os

#Dropbox Imports
import dropbox

#Google Drive Imports
import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

def verifyLogin():
    #Loads the user information 
    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
            authkey = json.dumps(userclouds)
            return userclouds
    except IOError:
        print "Please login first!"
        sys.exit()


def uploadNotChunked(fileName, service):
    userclouds = verifyLogin()

    if (service == 'dropbox'):
        dropbox.client.DropboxClient(userclouds['dropbox'][0], locale=None, rest_client=None).put_file("/VirtualCloud/" + os.path.basename(fileName), fileName)

    elif (service == 'drive'):

        # All code from Google's Example
        # Copy your credentials from the console
        # Do we have a drive API CLIENT ID?
        CLIENT_ID = 'YOUR_CLIENT_ID'
        CLIENT_SECRET = userclouds['gdrive'][0]

        # Check https://developers.google.com/drive/scopes for all available scopes
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

        # Redirect URI for installed apps
        REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

        # Path to the file to upload
        FILENAME = fileName

        # Run through the OAuth flow and retrieve credentials
        flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        print 'Go to the following link in your browser: ' + authorize_url
        code = raw_input('Enter verification code: ').strip()
        credentials = flow.step2_exchange(code)

        # Create an httplib2.Http object and authorize it with our credentials
        http = httplib2.Http()
        http = credentials.authorize(http)

        drive_service = build('drive', 'v2', http=http)

        # Insert a file
        media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
        body = {
        'title': 'My document',
        'description': 'A test document',
        'mimeType': 'text/plain'
        }

        file = drive_service.files().insert(body=body, media_body=media_body).execute()
        pprint.pprint(file)






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
