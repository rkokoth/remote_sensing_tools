import os
import random
import argparse

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mask_vector", help="please provide the path to shapefile that clips the other here.")
#parser.add_argument("destination_file", help="please provide the path to save the clipped file here.")
parser.add_argument("vector_to_clip", help="please provide the path to file to be clipped here.")
args = parser.parse_args()
#parser.parse_args()

def clip_vector_by_mask(mask_vector,vector_to_clip):
    print(os.path.split(vector_to_clip)[0])
    print(os.path.basename(vector_to_clip))
    BASE_DIR = os.path.split(vector_to_clip)[0]
    random_digits = random.randrange(0, 1000, 3)
    out_dir = f'clipped_{random_digits}' 
    if not os.path.isfile(out_dir):
        if not os.path.isdir(out_dir):
            os.mkdir(os.path.join(BASE_DIR,out_dir))

    if os.path.isdir(vector_to_clip):
        files_to_clip = [f for f in os.listdir(vector_to_clip) if f.endswith('.gpkg') or f.endswith('.shp')]

        for file in files_to_clip:
            infile = os.path.join(vector_to_clip,file)
            outfile = os.path.join(out_dir,f'cliped_{file}')
            bash_command = f'bash ogr2ogr_clip_vector_by_mask_layer.sh {str(mask_vector)} {str(outfile)} {str(infile)}'
            os.system(bash_command)
    else:
        file =os.path.basename(vector_to_clip)
        outfile = os.path.join(BASE_DIR,out_dir,f'clipped_{file}')
        bash_command = f'bash ogr2ogr_clip_vector_by_mask_layer.sh {str(mask_vector)} {str(outfile)} {str(vector_to_clip)}'
        print(bash_command)
        os.system(bash_command)




clip_vector_by_mask(args.mask_vector,args.vector_to_clip)