import os
try:
    import rasterio as rio 
    import numpy as np 
    import pandas as pd 
    import geopandas as gpd
except:
    os.system('pip install rasterio numpy pandas geopandas')
    import rasterio as rio 
    import numpy as np 
    import pandas as pd 
    import geopandas as gpd
import warnings
import argparse


warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
parser = argparse.ArgumentParser()
parser.add_argument("reference_raster", help="please provide the path to reference year classification raster.")
parser.add_argument("start_year_raster", help="please provide the path to year classification raste.")

parser.add_argument("forest_class_value", help="please provide the forest class value.")
parser.add_argument("non_forest_class_value", help="please the provide non forest class value.")
parser.add_argument("pixel_size", help="please the resolution of the input rasters.")
args = parser.parse_args()


def eligible_non_ligible_classification(reference_year_classification, start_year_classification, forest_class_value,non_forest_class_value,pixel_size):

    new_file_name = reference_year_classification.replace(os.path.basename(reference_year_classification),'eligible_non_eligible.tif')

    with rio.open(reference_year_classification, 'r') as src:
        reference_year_data = src.read()
        profile = src.profile
        profile['count'] = 1
        src.close()

    with rio.open(start_year_classification, 'r') as src:
        start_year_data = src.read()
        profile = src.profile
        profile['count'] = 1
        src.close()

    # Make sure reference and start year classification arrays are of the same shape
    # TODO: compare the shapes and clip larger shape with the smaller one. 
    start_year_data = start_year_data[:,:reference_year_data.shape[1],:reference_year_data.shape[2]]

    print(start_year_data.shape)
    print(reference_year_data.shape)

    # DEFINE ELIGIBILITY RULES HERE
    non_forest_class_value = int(non_forest_class_value)
    forest_class_value = int(forest_class_value)
    #non_forest_class_value = 2
    #forest_class_value = 1

    rule_1 = (reference_year_data == non_forest_class_value) & (start_year_data == non_forest_class_value) # consistent non forest eligible
    rule_2 = (reference_year_data == forest_class_value) & (start_year_data == forest_class_value) # consistent forest non elegible
    rule_3 = (reference_year_data == non_forest_class_value) & (start_year_data == forest_class_value) # non forest to forest not elegible
    rule_4 = (reference_year_data == forest_class_value) & (start_year_data == non_forest_class_value) # forest to non forest  NOT elegible

    # reclassify the two classification arrays and assign eligible pixels value 1 and non-eligible pixels value 2. value 0 is nodata
    eligible_pixels = np.select([rule_1,rule_2,rule_3,rule_4],[1,2,2,2],0)


    # write data to file.

    with rio.open(new_file_name, 'w', **profile) as dst:
            dst.write(eligible_pixels[0], 1)
            dst.close()

    pixel_count = np.unique(eligible_pixels, return_counts=True)
    print(pixel_count[1][2])
    pixel_size = float(pixel_size)


    eligble_area = pixel_count[1][1]*pixel_size*pixel_size/10e4
    non_eligible_area =  pixel_count[1][2]*pixel_size*pixel_size/10e4

    eligibility_df = pd.DataFrame({
         'eligible_area_ha': [eligble_area],
         'non_eligible_area_ha': [non_eligible_area]
    })

    print(f'eligibility raster saved successfully in {new_file_name}')

    return(eligibility_df)


if __name__ == "__main__":
     eligible_non_ligible_classification(reference_year_classification=args.reference_raster,
                                         start_year_classification=args.start_year_raster, 
                                         forest_class_value=args.forest_class_value,
                                         non_forest_class_value=args.non_forest_class_value,
                                         pixel_size=args.pixel_size)
     
