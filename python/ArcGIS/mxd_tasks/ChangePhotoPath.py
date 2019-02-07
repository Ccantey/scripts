import arcpy
mxd = arcpy.mapping.MapDocument(r"Q:\Geodata\Maps\PhotoMaps\2019\mxd\MNHouse19_photomap.mxd")
for elm in arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT"):
    #check image sources before running ChangePath
    #print elm.sourceImage

    #ChangePath
    if "\\2017\\" in elm.sourceImage:
        original = elm.sourceImage
        new = original.replace('\\2017\\', '\\Current\\')
        print new
        elm.sourceImage = new
        
mxd.save()
del mxd
