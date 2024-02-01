
# from rasterio.plot import show
# from rasterio.merge import merge
# import rasterio as rio
# from pathlib import Path
import os
import sys
import platform
import time

from osgeo import gdal
from osgeo import ogr
from osgeo import osr
from osgeo import gdal_array
from osgeo import gdalconst





# path = Path('.data/')
# Path('output').mkdir(parents=True, exist_ok=True)
# output_path = 'output/mosaic_output.tif'



# def mosaicRasters(path):
#     Path('output').mkdir(parents=True, exist_ok=True)
#     if os.path.isdir(path):
#         path = Path(path)
#         Path('output').mkdir(parents=True, exist_ok=True)
#     else:
#         print(f'There is no such directory as {path}')
#         sys.exit()
#     output_path = 'output/mosaic_output.tif'
#     raster_files = list(path.iterdir())
#     raster_to_mosiac = []

#     for p in raster_files:
#         raster = rio.open(p)
#         raster_to_mosiac.append(raster)

#     mosaic, output = merge(raster_to_mosiac)


#     output_meta = raster.meta.copy()
#     output_meta.update(
#         {"driver": "GTiff",
#             "height": mosaic.shape[1],
#             "width": mosaic.shape[2],
#             "transform": output,
#         }
#     )

#     with rio.open(output_path, 'w', **output_meta) as m:
#         m.write(mosaic)


# def gdal_mosaic(path):
#     os.chdir(path)
#     path = os.getcwd()
#     if platform.system() == 'Windows':
#         command = f'dir /b /s {path}\*.tif > {path}\list.txt'
#     else:
#         command = f'ls {path}/*.tif >> {path}/list.txt'
#     print(command)
#     os.system(command)
#     time.sleep(10)
#     os.chdir(path)
#     os.system(f'gdal_merge.py -o {path}/mosaic.tif --optfile list.txt')


def gdal_mosaic(path):
    files = [f for f in os.listdir(path) if f.endswith('.tif') or f.endswith('tiff')]
    print(files)
    g = gdal.Warp(os.path.join(path,"mosaic.tif"), files, format="GTiff")
    g = None # Close file and flush to disk
    

#gdal_mosaic(sys.argv[1])