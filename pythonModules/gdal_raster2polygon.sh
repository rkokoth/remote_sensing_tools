#!/usr/bin/bash
# input 1 = raster file to polygonize
# input 2 = output file fortmat. read here for available options("GPKG")
# input 2 = path to store the output

gdal_polygonize.py $1 -b 1 -f $2 -overwrite $3 "polygonised" "eligibility" 


#ogr2ogr -where "\"eligibility\" > 0" \ polygonised.gpkg $3

#rm -rfv $3

echo $3