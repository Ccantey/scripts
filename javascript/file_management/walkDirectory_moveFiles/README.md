  Node.js script to walk through a directory,
  read all the files, match files you are interested, 
  then copy and paste them to a new location.
  Used for Census block data which has the following 
  FIPS codes based directory setup:
    Shape/
      27001/
        PVS_17_v2_addr_27001.dbf, .shp, .shx, .prj
        PVS_17_v2_aial_77001.dbf, .shp, .shx, .prj
        etc..
      27003/
        etc....

  It requires the following node modules: walk

  > npm install --save walk
  > node walkDirs_moveFiles.js