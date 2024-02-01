#!/usr/bin/bash

# transforms the projection of an imput layer to user defined epsg code
# imput 1= epsg code (for new projection)
# input 2 = path to write the projected file
# input 3 = the vector file to project

ogr2ogr -t_srs EPSG:$1 $2 $3