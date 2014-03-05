import sys
import json
import db_ops
import gd_ops
import os

def login():
    try:
        with open(".virtualcloud", "w+") as json_data:
            data = json.load(json_data)
    except IOError:
        print "Could not create new settings file"

    if not data:
        data = {'dropbox' : [], 'gdrive' : []}
        
    while True:
        cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. When done, enter 'done': ").lower()
        if cmd == 'dropbox':
            db = db_ops.db(-1)
            data['dropbox'].append(ndb.AT)          
        if cmd == 'gdrive':
            gd = gd_ops.gd(-1)
            data['gdrive'].append(ngd.credentials)        
        if cmd == 'done':
            break

    try:
        with open(".virtualcloud", "w+") as json_file:
            json.dump(data,json_file)
    except IOError:
        print "Sorry, failed to add accounts!"
        sys.exit()


    
    

