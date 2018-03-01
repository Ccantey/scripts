import os

for root, dirs, files in os.walk(r"C:\Users\ccantey\Desktop\WhoRepsPhotos\resizedHouse"):

    for filename in files:
        
        #Change from 03Ekken.jpb to 03.jpg
        #print filename[:2]
        #file_extension = os.path.splitext(filename)
        #print file_extension[-1]
        #os.rename(root + os.sep + filename, root + os.sep + filename[:2] + file_extension[-1])
        
        # change name from tn_03.jpg to 03.jpg
        print filename[3:]
        os.rename(root + os.sep + filename, root + os.sep + filename[3:])
        
        
