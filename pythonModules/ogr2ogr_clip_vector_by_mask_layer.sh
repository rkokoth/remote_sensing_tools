#!/usr/bin/bash
ogr2ogr -clipsrc  $1  $2  $3

echo  'clipped file created in ' $2