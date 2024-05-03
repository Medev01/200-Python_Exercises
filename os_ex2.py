import os
 
 
base_dir = 'images'
png_dir = os.path.join(base_dir, 'images_png')
jpg_dir = os.path.join(base_dir, 'images_jpg')
 
if not os.path.exists(base_dir):
    os.mkdir(base_dir)
 
if not os.path.exists(png_dir):
    os.mkdir(png_dir)
 
if not os.path.exists(jpg_dir):
    os.mkdir(jpg_dir)

'''
os.walk() is a function in Python's os module that allows you 
to iterate over a directory tree, generating the filenames 
in a directory tree by walking the tree either top-down or bottom-up.
''' 
for root, dirs, files in os.walk(base_dir):
    print(root)