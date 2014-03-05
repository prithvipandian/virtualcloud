import sys
import json
import db_ops
import gd_ops

def login():
    data = ""

    if os.path.isfile('.virtualcloud') == True:
        try:
            json_data = open(".virtualcloud", "r+")
        except e:
            print 'failed to open settings file'                     
        
        try:    
            data = json.load(".virtualcloud")
        except e:
            print 'failed to load settings file'    
        
        try:        
            json_data.close()
        except e:
            print 'failed to close settings file'    

    else:
        data = {
                    'dropbox' : [], # List of db tokens
                    'gdrive' : [] # List of gd tokens
               }
        

    while True:

        cmd = raw_input("To add a service please enter 'dropbox' or 'gdrive'. To go back enter 'back': ")
        cmd.lower()
        if cmd == 'dropbox':
            ndb = db_ops.db(-1)
            data['dropbox'].append(ndb.AT)
            
        if cmd == 'gdrive':
            ngd = gd_ops.gd(-1)
            data['gdrive'].append(ngd.credentials)
        
        if cmd == 'back':
            break


    json_data = json.dump(data)

    try:
        json_file = open('.virtualcloud', w)
    except e:
        'filed to open/create settings file'    

    try:
        json_file.write(json_data)
    except:
        print'failed to write to settings file'

    try:
        json_file.close()
    except e:
        print'failed to close settings file'



    
    

