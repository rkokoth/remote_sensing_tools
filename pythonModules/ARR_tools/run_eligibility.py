import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("resolution", help="please provide resampling resolution.")
parser.add_argument("mode", help="please specify what resampling algorithm is best to use (mode, nearest, ...).")
parser.add_argument("inRaster", help="please specify the raster to be resampled here.")
parser.add_argument("outRaster", help="please specify where to store the resampled raster.")

parser.add_argument("reference_raster", help="please provide the path to reference year classification raster.")
parser.add_argument("start_year_raster", help="please provide the path to year classification raste.")
parser.add_argument("mask_vector", help="please provide the path to shapefile that clips the other here.")

parser.add_argument("vector_to_clip", help="please provide the path to file to be clipped here.")


args = parser.parse_args()


os.system(f'python3 ../resample_raster_gdalTranslate.py {args.resolution} {args.mode} {args.inRaster} {args.outRaster}')

os.system(f'python3 compute_eligibility_raster.py {args.reference_raster} {args.start_year_raster} {args.resolution}')

os.system(f'python3 ../clip_vector_byMaskLayer_OGR.py {args.mask_vector} {args.vector_to_clip}')

clip_vector_by_mask(args.mask_vector,args.vector_to_clip)