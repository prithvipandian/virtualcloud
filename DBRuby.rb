# Install this the SDK with "gem install dropbox-sdk"
require 'dropbox_sdk'

puts "Welcome to VirtualCloud!"

# Get your app key and secret from the Dropbox developer website
APP_KEY = 'pp92jonnw43vmz8'
APP_SECRET = 'il7w6zl9blvejok'

flow = DropboxOAuth2FlowNoRedirect.new(APP_KEY, APP_SECRET)

authorize_url = flow.start()

# Have the user sign in and authorize this app
puts '1. Go to: ' + authorize_url
puts '2. Click "Allow" (you might have to log in first)'
puts '3. Copy the authorization code'
print 'Enter the authorization code here: '
code = gets.strip

# This will fail if the user gave us an invalid authorization code
access_token, user_id = flow.finish(code)

client = DropboxClient.new(access_token)
puts "linked account:", client.account_info().inspect
