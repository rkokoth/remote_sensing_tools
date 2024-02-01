#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

# import datetime
import geopandas as gpd 
import os
import sys
import numpy as np

def getProductURL(product_name):
    url_endpoint = 'https://storage.googleapis.com/earthenginepartners-hansen/GFC-2022-v1.10/download.html'
    r = requests.get(url_endpoint)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find_all('a')
    product = product_name
    for row in table:
        if str(row['href']).endswith(f'{product.lower()}.txt'):
            product_url = str(row['href'])
            #print(row['href'])
    return product_url

#print(getProductURL('lossyear'))
def get_tiles_list(product_url,product_name):
    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find_all('body')
    x = str(table[0]).replace('<body>','').replace('</body>','')
    x = x.strip()
    x = x.split('\n')
    #with open(f'{product_name}_{datetime.datetime.now()}.txt') as f:
        #f.write(x)
        #f.close()
    return(x)

def chooseTile(roi,product_name):
    if isinstance(roi, gpd.GeoDataFrame):
        roi = roi
        print('Extracting BBOX from a geopandas dataframe')
        
    elif os.path.isfile(roi):
       print('Reagaing BBOX from a file')
       roi = gpd.read_file(roi)
    else:
        print('roi must be a geopandas dataframe or a path to geospatial file')
        sys.exit()
    minx,miny,maxx, maxy = roi.total_bounds

    tile_ur_list = get_tiles_list(getProductURL(product_name),product_name)

    pattern = get_tile_list_to_download(minx,miny,maxx, maxy)
   
    chosen = []
    for tile in tile_ur_list:
        for p in pattern:
            if p in tile:
                chosen.append(tile)

    print(chosen)
    return(chosen)

#get_tiles_list(getProductURL('lossyear'),'lossyear')
        
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

def isnegative(number):
    if number < 0:
        return True
    else:
        return False



def downloadHanseTile(url, file_name):

    #command = f'sudo wget -P {path} {product_url}/{tile}/{x}'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join('.',file_name), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)


def getData(roi, product_name):
    if not os.path.isdir(os.path.join(os.path.dirname(__file__),product_name)):
        os.mkdir(os.path.join(os.path.dirname(__file__),product_name))

    dir_name = os.path.join(os.path.dirname(__file__),product_name)
    
    for url in chooseTile(roi,product_name):
        file_name = url.split('/')[-1]
        file_name = os.path.join(dir_name,file_name)
        print(file_name)
        downloadHanseTile(url,file_name)

if __name__ == '__main__':
    import mergeRasterio as mr
    import time
    path = './data/ZambiaPolygon_test.shp'
    getData(path, 'lossyear')
    #time.sleep(20)
    mr.gdal_mosaic('./lossyear')
    