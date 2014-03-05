import cmd
from upload import upload
from download import download
from login import login
from logout import logout


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
    def do_login(self, *args):
        'Login with username and password'
        login()
    def do_upload(self, fn, cs):
        'Upload to one or both accounts from local'
        upload(fn, cs)
    def do_download(self, *args):
        'Download from accounts to local'
        download(args)
    def do_logout(self, *args):
        'Logout and erase all user data'
        logout()
    def do_ls(self, *args):
        'List all files in current directory'
        #list(args)
        pass
    def do_mkdir(self, *args):
        pass

