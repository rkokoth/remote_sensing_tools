import geopandas as gpd 
import numpy as np 
test_roi = '../../FS_ZM_001_WV/planet_test/ZambiaPolygon.shp'

minx,miny,maxx, maxy = gpd.read_file(test_roi).total_bounds
print(minx,miny,maxx, maxy)

def find_tiles_overlapping_roi(minx,miny,maxx, maxy):
    # this point is sure downloaded
    top_left = [maxy,minx]
    bottom_left = [miny,minx]
    # here compare the y dimention because x does not change

def identify_tile(x,y):
    '''
    Identifies on which tile each corner point of a bounding box falls based on HansenData tiling. 
    
    '''
    lat = str(int(np.floor(abs(y))))
    lon = str(int(np.floor(abs(x))))

    lat = int(lat.replace(lat[-1], '0'))
    lon = int(lon.replace(lon[-1], '0'))
    print(lat, lon)
    return [lat, lon]

def assignDirection(coord_value, type_):
    if isnegative(coord_value):
        if type_ == 'longitude':
            direction = 'W'
        else:
            direction = 'S'
    else:
        if type_ == 'longitude':
            direction = 'E'
        else:
            direction = 'N'
    return(direction)
def get_tile_list_to_download(minx,miny,maxx, maxy):
    tiles_to_get = []
    top_left = [minx,maxy]
    bottom_left = [minx, miny]
    bottom_right = [maxx,miny]
    top_right = [maxx,maxy]
    corners = [top_left, bottom_left, bottom_right,top_right]

    for corner in corners:
        x,y = corner
        tile_id = top_left_conner(x,y)
        tiles_to_get.append(tile_id)

    return(np.unique(tiles_to_get))





def isnegative(number):
    if number < 0:
        return True
    else:
        return False

def top_left_conner(x,y):
    '''
    Identifies on which tile each corner point of a bounding box falls based on HansenData tiling. 
    
    '''

    x_location = assignDirection(x,'longitude')
    y_location = assignDirection(y,'latitude')

    lat = str(int(np.floor(abs(y))))
    lon = str(int(np.floor(abs(x))))

    lat = int(lat.replace(lat[-1], '0'))
    lon = int(lon.replace(lon[-1], '0'))
    #print(lat, lon)
    
    if int(lon)<100:
        lon = '0' + str(lon)
    #print(f'_{lat}{y_location}_{lon}{x_location}')
    return(f'_{lat}{y_location}_{lon}{x_location}')
