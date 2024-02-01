import os
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("new_resolution", help="please provide new_resolution to resample the raster to.")
parser.add_argument("mode", help="please specify what resampling algorithm is best to use (mode, nearest, ...).")
parser.add_argument("inRaster", help="please specify the raster to be resampled here.")
parser.add_argument("outRaster", help="please specify where to store the resampled raster.")
parser.add_argument("reproject", help="Please specify why you need to reproject the raster before resampling.",default=False)
parser.add_argument("CRS", help="pBecayse you have specified thst you need to reproject the raster before resampling, yopu need to specify the new CRS.",default=None)
args = parser.parse_args()


def resample_raster(new_resolution, mode, inRaster, outRaster,reproject):

    """
    Resamples a raster image to a new resolution using GDAL.

    Args:
        new_resolution (float): The desired resolution of the resampled raster.
        mode (str): The resampling mode to be used. Options are 'nearest', 'bilinear', 'cubic', 'cubicspline', 'lanczos', 'average', 'mode', 'max', 'min', 'med', 'q1', 'q3'.
        inRaster (str): The input raster file or directory containing raster files.
        outRaster (str): The output directory for the resampled raster files.
        reproject (bool): Indicates whether to reproject the raster before resampling.

    Returns:
        None
    """
    _,ext = os.path.splitext(outRaster)
    if not ext:
        if not os.path.isdir(outRaster):
            os.mkdir(outRaster)
    if os.path.isdir(inRaster):
        tif_files = [f for f in os.listdir(inRaster) if f.endswith('.tif') or f.endswith('.tiff')]
        print(tif_files)

        for file in tif_files:
            if bool(reproject) == True:
                infile_to_project = os.path.join(inRaster,file)
                outfile_projected = os.path.join(inRaster,f'projected_{file}')
                os.system(f'bash gdalwarp_reprojectRaster.sh {str(args.CRS)} {infile_to_project} {outfile_projected}')
                time.sleep(3)
            else:
                infile_to_project = os.path.join(inRaster,file)

            infile = outfile_projected
            outfile = os.path.join(outRaster,f'resampled_{file}')
            bash_command = f'bash resample_raster.sh {float(new_resolution)} {str(mode)} {str(infile)} {str(outfile)}'
            os.system(bash_command)
    else:
        if bool(reproject) == True:
            n,_extention = os.path.splitext(inRaster)
            infile_to_project = inRaster
            outfile_projected = inRaster.replace(_extention, f'_projcted{_extention}')
            os.system(f'bash gdalwarp_reprojectRaster.sh {str(args.CRS)} {infile_to_project} {outfile_projected}')
            time.sleep(3)

        else:
            infile_to_project = inRaster

        infile = infile_to_project
        bash_command = f'bash resample_raster.sh {float(new_resolution)} {str(mode)} {str(inRaster)} {str(outRaster)}'
        os.system(bash_command)
    print(bash_command)

if __name__ == '__main__':
    resample_raster(args.new_resolution,args.mode,args.inRaster,args.outRaster, args.reproject)