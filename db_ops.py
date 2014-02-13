# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'pp92jonnw43vmz8'
app_secret = 'il7w6zl9blvejok'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

def db_login():
    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()

    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)

    client = dropbox.client.DropboxClient(access_token)
    print 'linked account: ', client.account_info()

def db_upload(user_file):
    f = open(userfile, 'rb')
    response = client.put_file('/' + user_file, f)
    print 'uploaded: ', response

folder_metadata = client.metadata('/')
print 'metadata: ', folder_metadata

f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata
