import os
rootdir = 'D:\DDP Test\All-new name\copy'

for root, dirs, files in os.walk(rootdir):
    for pdfs in files:
        if pdfs.count('+') == 2:
            print pdfs

