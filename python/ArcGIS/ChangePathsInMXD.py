import arcpy, os

#walk through all subdirectories and change mxd to store relative paths


mxd = arcpy.mapping.MapDocument(r"Q:\Geodata\Maps\PhotoMaps\2017\house\mxd\MNHouse16_photos.mxd") 
mxd.findAndReplaceWorkspacePaths(r"Q:\Geodata\graphics\hseFeb2015", r"Q:\Geodata\Graphics\House Photos\2017") 
mxd.saveACopy(r"Q:\Geodata\Maps\PhotoMaps\2017\house\mxd\MNHouse17_photos.mxd")
del mxd

                

