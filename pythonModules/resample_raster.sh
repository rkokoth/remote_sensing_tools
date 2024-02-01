#!/usr/bin/bash
# inputs 1: new resolution
# input 2: resampling modes (accepted are: nearest, mode,cubic, ....) check here:
# input 3: path to raster to resample
# input 4: path to where resampled should be stored

gdal_translate -tr $1 $1 -r $2 $3 $4
