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
        #setup()
        pass
    def do_login(self):
        'Login with username and password'
        db_ops.db_login()
    def do_upload(self, *args):
        'Upload to one or both accounts from local'
        upload(args)
        pass
    def do_download(self, *args):
        'Download from accounts to local'
        download(args)
    def do_ls(self, *args):
        'List all files in current directory'
        #list(args)
        pass
    def do_mkdir(self, *args):
        pass

