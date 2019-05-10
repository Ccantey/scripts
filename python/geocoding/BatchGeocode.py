import csv
import os
from geopy.geocoders import GoogleV3
from Tkinter import Tk
from tkFileDialog import askopenfilename
from xlsxwriter.workbook import Workbook
geolocator = GoogleV3('### YOUR GOOGLE API KEY: https://console.developers.google.com/apis ###')

###BasicAPI
##location = geolocator.geocode('10351 Ash River Trail Orr MN')
##print location.latitude

#Open Browser window, Open CSV file
Tk().withdraw()
filename = askopenfilename(initialdir = "Q:\Geodata\Projects\Projects2019",filetypes=[("CSV Files",".csv")])

#Create output file name
dirPath = os.path.dirname(filename)
baseNameWithExt = os.path.basename(filename)
baseName = os.path.splitext(baseNameWithExt)[0]
outputFileName = os.path.join(dirPath, baseName + "_XY.csv")

# some csv file with a minimum of an address field, city field, zip code field
with open(filename, 'rb')as csvinput:
    # output file/location
    with open(outputFileName, 'w') as csvoutput:
        reader = csv.DictReader(csvinput, delimiter=',')

        #All the output column headers :
        columns = reader.fieldnames
        columns.append('Latitude')
        columns.append('Longitude')
        #print columns
        
        writer = csv.DictWriter(csvoutput, fieldnames=columns, lineterminator='\n')
        writer.writeheader()  
  
        for row in reader:
            #The only thing you need to change is how we compile the full address - columns vary from csv to csv
            fullAddress = row["Address"] + ', ' + row["City"]+ ', ' + row["State"]+ ' ' + row["Zip"]
            print fullAddress
            #customID not necessary - but would need to change print out at end.
            customID = row["Last Name"]
            location = geolocator.geocode(fullAddress, timeout=10)
            

            try:
                geocodelatitude = location.latitude
                geocodelongitude =location.longitude
                Lat = str(geocodelatitude)
                Long =str(geocodelongitude)
                LatLong = str(geocodelatitude) + '|' + str(geocodelongitude)
                #writer.writerow({'Latitude': Lat,"Longitude":Long})
                row['Latitude'] = Lat
                row['Longitude'] = Long
                writer.writerow(row)
                #writer.writerow({'Last Name':row["Last Name"], 'First Name':row["First Name"], 'Middle Name':row["Middle Name"],'Address':row["Address"], 'City':row["City"],'State':row["State"],'ZIP':row["ZIP"],'Latitude': Lat,"Longitude":Long})

                
            except:
                geocodelatitude = 'No Match'
                geocodelongitude = 'No Match'
                Lat = 'No Match'
                Long = 'No Match'
                writer.writerow({'Latitude': Lat,"Longitude":Long})
                LatLong = str(geocodelatitude) + '|' + str(geocodelongitude)
                #writer.writerow({'Latitude': Lat,"Longitude":Long})
                row['Latitude'] = Lat
                row['Longitude'] = Long
                writer.writerow(row)
                #row looks like this:
                #writer.writerow({'Last Name':row["Last Name"], 'First Name':row["First Name"], 'Middle Name':row["Middle Name"],'Address':row["Address"], 'City':row["City"],'State':row["State"],'ZIP':row["ZIP"],'Latitude': Lat,"Longitude":Long})

            print "Name", str(customID),", Latitude", str(geocodelatitude),", Longitude", str(geocodelongitude)

#OPTIONALLY CONVERT OUTPUT TO EXCEL
#Convert the csv to xlsx: ArcGIS and QGIS seem to prefer CSVs, Maptitude needs xlsx
workbook = Workbook(outputFileName[:-4] + '.xlsx', {'strings_to_numbers': True})
worksheet = workbook.add_worksheet()
with open(outputFileName, 'r') as f:
    reader = csv.reader(f)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r, c, col)
workbook.close()
#Remove CSV
os.remove(outputFileName)
print
print "Finished! Results: " + outputFileName[:-4] + '.xlsx'