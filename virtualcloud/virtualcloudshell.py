import cmd
from setup import setup
from upload import upload
from download import download
from login import login
from logout import logout
from makedir import mkdir
from makedir import getName


class VirtualCloudShell (cmd.Cmd):
    intro = 'Welcome to VirtualCloud! Type help or ? to list commands.\n'
    prompt = '(virtualcloud)'

    #------ basic virtualcloud commands ---------
    def do_setup(self, arg):
        '''Setup your virtualcloud account with Dropbox and/or Google Drive. 
        Add and remove accounts.
        This must be run at least once for anything else to work.
        '''
        setup()
    def do_upload(self, arg):
        'Upload to one or both accounts from local. Usage: "upload <full file path> <chunksize>" '
        upload(*parse(arg))
    def do_download(self, arg):
        'Download from accounts to local current directory. Usage: "download <filename>"'
        download(*parse(arg))
    def do_ls(self, arg):
        'List all files in current directory'
        #list(args)
        pass
    def do_mkdir(self, arg):
    	'Create a folder'
        mkdir(arg)
        pass

def parse(arg):
    return tuple(arg.split())
