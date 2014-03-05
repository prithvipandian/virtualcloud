#!/usr/bin/python
 
import httplib2
import pprint
 
from apiclient import errors
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
 
 
# Copy your credentials from the console
CLIENT_ID = '870106712178-889u4uppc9eqg9nn6prto4cja7dn3g25.apps.googleusercontent.com'
CLIENT_SECRET = '2uS8GNwONT_qq_0gHoL1Xpxi'
 
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
 
# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

class gd(object):
    
    drive_service = 0
    credentials = 0
    
    def __init__(self, token):
        self.credentials = token
        if self.credentials == -1:
            self.gd_login()
        else:
            http = httplib2.Http()
            http = credentials.authorize(http)
            self.drive_service = build('drive', 'v2', http=http)
 
    def gd_login(self):
        flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        print 'Go to the following link in your browser: ' + authorize_url
        code = raw_input('Enter verification code: ').strip()
        self.credentials = flow.step2_exchange(code)
        http = httplib2.Http()
        http = self.credentials.authorize(http)
        self.drive_service = build('drive', 'v2', http=http)

    def gd_upload(self, user_file):
         # Insert a file
         media_body = MediaFileUpload(user_file, mimetype='text/plain', resumable=True)
         body = {
           'title': 'username',
           'description': '',
           'mimeType': 'text/plain'
         }
         file = self.drive_service.files().insert(body=body, media_body=media_body).execute()
         pprint.pprint(file)
        
    def gd_download(self, user_file):
        download_url = user_file.get('downloadUrl')
        if download_url:
            resp, content = self.drive_service._http.request(download_url)
            if resp.status == 200:
                print 'Status: %s' % resp
                return content
            else:
                print 'An error occurred: %s' % resp
                return None
        else:
            # The file doesn't have any content stored on Drive.
            return None

random = gd(-1)
random.gd_upload('README.md')
random.gd_download('README.md')
