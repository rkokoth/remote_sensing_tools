#! /bin/bash
# input 1 is the vector to mask raster with
# input2 is the raster to clip
#input3 is the  output file name

AU_NAME=AU_MSM3-3.7-00.01.02.03
x=$1
x2=${x##*/}
#gdalwarp -overwrite -of GTiff -cutline $1 -cl ${x2%%.*} -crop_to_cutline $2 $3
#awk -F: '{print $1}'
echo ${x2%%.*}