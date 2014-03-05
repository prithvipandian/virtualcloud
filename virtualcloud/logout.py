import os.path

def logout():
    try:
        os.remove(".virtualcloud")
    except OSError:
        print 'no file found to delete'

