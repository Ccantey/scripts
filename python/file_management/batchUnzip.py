import zipfile
import glob
import os


directory = glob.glob("Q:\Geodata\Projects\Projects2018\RepSheldonJohnson\shp\*.zip")

for files in directory:
##    print files
    outpath = os.path.splitext(files)[0]
    print outpath
    zfile = zipfile.ZipFile(files)
    try:
        for zips in zfile.namelist():
          #print zips
         
          zfile.extract(zips, outpath)
          print zips
    except:
        pass

