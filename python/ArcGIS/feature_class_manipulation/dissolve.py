# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "2012generalresults"
# Run inside mxd with the following fields: MNLEGDIS, MNSENDIST, CONGDIST, MCDNAME, COUNTYFIPS
arcpy.Dissolve_management(in_features="2012generalresults", out_feature_class="C:/Users/ccantey/Desktop/Mapbox Studio/combinedElection2012/2012mnhouseresults.shp", dissolve_field="MNLEGDIST", statistics_fields="USPRSR SUM;USPRSDFL SUM;USPRSLIB SUM;USPRSSWP SUM;USPRSCP SUM;USPRSCG SUM;USPRSGP SUM;USPRSGR SUM;USPRSSL SUM;USPRSJP SUM;USPRSWI SUM;USPRSTOTAL SUM;USSENIP SUM;USSENR SUM;USSENDFL SUM;USSENGR SUM;USSENMOP SUM;USSENWI SUM;USSENTOTAL SUM;USREPIP SUM;USREPR SUM;USREPDFL SUM;USREPWI SUM;USREPTOTAL SUM;MNSENIP SUM;MNSENR SUM;MNSENDFL SUM;MNSENWI SUM;MNSENTOTAL SUM;MNLEGIP SUM;MNLEGR SUM;MNLEGDFL SUM;MNLEGWI SUM;MNLEGTOTAL SUM", multi_part="MULTI_PART", unsplit_lines="DISSOLVE_LINES")
