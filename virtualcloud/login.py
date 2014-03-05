import sys
import json
import db_ops
import gd_ops
import os

def login():
    data = ""

    try:
        with open(".virtualcloud", "r+") as json_data:
            data = json.load(json_data)
    except IOError:
        print "Creating new settings file"
        data = {'dropbox' : [], 'gdrive' : []}
        continue

    while True:
        cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. To go back enter 'back': ")
        cmd.lower()
        if cmd == 'dropbox':
            db = db_ops.db(-1)
            data['dropbox'].append(ndb.AT)          
        if cmd == 'gdrive':
            gd = gd_ops.gd(-1)
            data['gdrive'].append(ngd.credentials)        
        if cmd == 'back':
            break

    try:
        os.remove(".virtualcloud")
        with open(".virtualcloud", "w+") as json_file:
            json.dump(data,json_file)
    except IOError:
        print "Sorry, failed to add accounts!"
        sys.exit()


    
    

