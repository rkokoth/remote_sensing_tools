#!/usr/bin/bash
# inputs 1: new CRS to reprojct the raster to
# input 2: Raster to reproject
# input 3: where to store the reprojected file

gdalwarp -t_srs EPSG:$1 $2 $3