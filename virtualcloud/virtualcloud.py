import cmd
from virtualcloud import *

class VirtualCloudShell (cmd.Cmd):
    intro = 'Welcome to VirtualCloud! Type help or ? to list commands.\n'
    prompt = '(virtualcloud)'

    #------ basic virtualcloud commands ---------
    def do_setup(self):
        '''
        Setup your virtualcloud account with Dropbox and/or Google Drive. 
        This must be run at least once for anything else to work.
        '''
        setup()
    def do_login(self, *args):
        'Login with username and password'
        login(args)
    def do_upload(self, *args):
        'Upload to one or both accounts from local'
        upload(args)
    def do_download(self, *args):
        'Download from accounts to local'
        download(args)

