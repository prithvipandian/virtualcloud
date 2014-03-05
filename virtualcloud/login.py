#Create file with Empty JSON

import sys, os.path, json

from db_ops import db
from gd_ops import gd

data = ""

if os.path.isfile('.virtualcloud') == True:
    
    json_data = open(".virtualcloud", "r+")
    data = json.load(".virtualcloud")
    json_data.close()
    
else:
    data = {
                'dropbox' : [], # List of db tokens
                'gdrive' : [] # List of gd tokens
           }
    

while True:

    cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. To go back enter 'back': ")
    cmd.lower()
    if cmd == 'dropbox':
        ndb = db(-1)
        ndb.db_login()
        data['dropbox'].append(nbd.AT)
        
    if cmd == 'gdrive':
        ngd = gd(-1)
        ngd.gd_login()
        data['gdrive'].append(ngd.AT)
    
    if cmd == 'back':
        break


data = json.dump(data)
json_data = open('.virtualcloud', w)
json_data.write(dump)
json_data.close()



    
    

