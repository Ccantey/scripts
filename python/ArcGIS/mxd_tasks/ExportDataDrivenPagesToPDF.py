import arcpy
import re
from arcpy import env
import os.path
env.workspace = "Q:\\Geodata\\shape\\house"

sCur = arcpy.SearchCursor("Q:\\Geodata\\shape\\house\\hse2012_vtd2015.shp")

# Fetch each feature from the cursor and examine the extent properties
#
for row in sCur:
    #clean bad characters out of fields
    #ceanName = re.sub('[^\w\-_\. ]', '_', row.PCTNAME)
    #Duplicate pct names, append county name
    ceanName = re.sub('[^\w\-_\. ]', '_', row.MNLEGDIST)

##    print row.PCTNAME
##    print ceanName
##    print

    geom = row.shape
    ext = geom.extent

    xlength = ext.XMax - ext.XMin
    ylength = ext.YMax - ext.YMin


    if xlength > ylength:
        print"x>y, map should be landscape"
        
        #skip if the file already exists - this is a long running script so breaks happen and we have to start over
        if os.path.isfile(r"D:\\LegislativeDistricts\\DDP House\\Landscape\\" + str(ceanName) + ".pdf"):
            print str(ceanName) + ".pdf exists"
        else:
            print str(ceanName) + ".pdf DOES NOT exist"
        
            mxd = arcpy.mapping.MapDocument(r"Q:\\Geodata\\Maps\House\\districts\\2018\\mxd\\HouseDistricts_Landscape_vtd.mxd")
            pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.MNLEGDIST))
            mxd.dataDrivenPages.currentPageID = pageID       
            print "Exporting landscape page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
            print str(row.MNLEGDIST) + ".pdf"
            print
            arcpy.mapping.ExportToPDF(mxd, r"D:\\LegislativeDistricts\\DDP House\\Landscape\\" + str(ceanName) + ".pdf",resolution=150)

            del mxd

    else:
        print"x<y, map should be portrait"

        #skip if the file already exists - this is a long running script so breaks happen and we have to start over
        if os.path.isfile(r"D:\\LegislativeDistricts\\DDP House\\Portrait\\" + str(ceanName) + ".pdf"):
            print str(ceanName) + ".pdf exists"
        else:
            print str(ceanName) + ".pdf DOES NOT exist"
            mxd = arcpy.mapping.MapDocument(r"Q:\\Geodata\\Maps\House\\districts\\2018\\mxd\\HouseDistricts_Portrait_vtd.mxd")
            pageID = mxd.dataDrivenPages.getPageIDFromName(str(row.MNLEGDIST))
            mxd.dataDrivenPages.currentPageID = pageID        
            print "Exporting portrait page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
            print str(row.MNLEGDIST) + ".pdf"
            print
            arcpy.mapping.ExportToPDF(mxd, r"D:\\LegislativeDistricts\\DDP House\\Portrait\\" + str(ceanName) + ".pdf",resolution=150)
            del mxd

