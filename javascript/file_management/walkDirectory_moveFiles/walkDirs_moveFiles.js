/*
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

*/

(function () {
  "use strict";
 
  var walk = require('walk')
    , fs = require('fs')
    , walker
    ;
 
  walker = walk.walk("D:\Shape");
 
  walker.on("directory", function (root, dirStats, next) {
    var path = root+'\\'+ dirStats.name;
    
    fs.readdir(path, function(err, items) {
        // console.log(dirStats.name);     
        for (var i=1; i<items.length; i++) {
            // console.log(items[i].split('.')[0]);
            var filename = items[i].split('.')[0];
            //'faces' == blocks
            if(filename.match('PVS_17_v2_faces_')){
              console.log(path+'\\'+items[i])
              console.log('D:CensusBlocks\\'+items[i])
              //copy and paste
              fs.createReadStream(path+'\\'+items[i]).pipe(fs.createWriteStream('D:CensusBlocks\\'+items[i]));
            }
        }
    }); 
    next();
  });
 
  walker.on("errors", function (root, nodeStatsArray, next) {
    next();
  });
 
  walker.on("end", function () {
    console.log("all done");
  });
}())