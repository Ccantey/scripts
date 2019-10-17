'''
This python scripts
1. Downloads NOAA historical 5km grid tar.gz files from FTP
2. Extracts the tar.gz into point files
3. Sorts the point files into directories: (prcp, tave, tmax, tmin)
'''

import zipfile
import glob
import os
from ftplib import FTP
import tarfile
import shutil


ftp = FTP('ftp.ncdc.noaa.gov')
ftp.login()
ftp.cwd('pub/data/climgrid')

workingDirectory = 'D:\\NOAA'
outputDirectory = 'D:\\NOAA\\output'

# get filenames within the directory
filenames = ftp.nlst()
#print filenames

counter = 0
for filename in filenames:
    counter +=1
    print filename
    print counter
    local_filename = os.path.join(workingDirectory, filename)
    file = open(local_filename, 'wb')
    ftp.retrbinary('RETR '+ filename, file.write)
    file.close()

ftp.quit()

print
print 'File download complete'
print
print 'Extracting contents'
print

counter = 0
for root, dirs, files in os.walk(workingDirectory):

    for tars in files:
        counter +=1
        print tars
        try:
            print counter
            tar = tarfile.open(os.path.join(root,tars), 'r:gz')
            tar.extractall(path=outputDirectory)
            tar.close()
        except:
            print '################ PASS ###################'
            pass


print
print 'File extraction complete'
print
print 'Moving contents'
print

counter = 0
for root, dirs, files in os.walk(outputDirectory):

    for pointfiles in files:
        counter +=1
        #print pointfiles
        try:
            print counter
            if 'prcp' in pointfiles:
                orig = os.path.join(root,pointfiles)
                new = os.path.join(root,'prcp',pointfiles)
                shutil.move(orig, new)

            elif 'tave' in pointfiles:
                orig = os.path.join(root,pointfiles)
                new = os.path.join(root,'tave',pointfiles)
                shutil.move(orig, new)
            elif 'tmax' in pointfiles:
                orig = os.path.join(root,pointfiles)
                new = os.path.join(root,'tmax',pointfiles)
                shutil.move(orig, new)
            elif 'tmin' in pointfiles:
                orig = os.path.join(root,pointfiles)
                new = os.path.join(root,'tmin',pointfiles)
                shutil.move(orig, new)
            else:
                break
         
        except:
            print '################ PASS ###################'
            pass

