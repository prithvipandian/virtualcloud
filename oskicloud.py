import dropbox, db_ops, hashlib, uuid
    
def entry():
    print 'Please enter a command'
    command = input(">")
    command.lower()
    cmds = command.split
    if command[0] in options:
        options[cmd[0]](cmds[1:])
    else:
        print 'Invalid command'

def upload(cmds):
    if cmds[0] in UL:
        UL[cmds[0]](cmds[1:])
    else:
        print 'invalid service'

def download(cmds):
    if cmds[0] in UL:
        UL[cmds[0]](cmds[1:])
    else:
        print 'invalid service'

#Intro
print 'Welcome to OskiCloud!'
print 'Login or 
LOR = 
#Login
username = raw_input('username: ')
password = raw_input('password: ')
print 'Welcome ' + username + '!'

#We need to implement a database for a users and their uthentication tokens.

options = {'upload': upload, 'download': download}
UL = {'dropbox': db_upload, 'gdrive': 1}
#User_Info = {
    
    
    


    


    
    
    
