import sys
import json
import db_ops
import gd_ops

def login():
    try:
        with open(".virtualcloud", "w+") as json_data:
            try: 
                data = json.load(json_data)
            except ValueError:
                data = {}
    except IOError:
        print "Could not create new settings file"

    if not data:
        data = {'dropbox' : [], 'gdrive' : []}
        
    while True:
        cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. When done, enter 'done': ").lower()
        if cmd == 'dropbox':
            db = db_ops.db(-1)
            data['dropbox'].append(db.AT)          
        if cmd == 'gdrive':
            gd = gd_ops.gd(-1)
            data['gdrive'].append(gd.credentials)        
        if cmd == 'done':
            break

    try:
        with open(".virtualcloud", "w+") as json_file:
            json.dump(data,json_file)
    except IOError:
        print "Sorry, failed to add accounts!"
        sys.exit()


    
    

