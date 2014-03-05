import os.path

try:
    os.remove(".virtualcloud")
except OSError:
    print 'no file found to delete'

