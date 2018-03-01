import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\Users\ccantey\Desktop\Graphics\Cartographic Work & Wireframes\Aiden_Twin_Citeis.mxd")
for elm in arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT"):
    print "found element"
    #if elm.name == "Photo":
    elm.sourceImage = r"Q:\Geodata\Graphics\logos\LCC-GIS\LCC-GIS-box_small_for GIS.png"
    print "changed source"
mxd.save()
del mxd
