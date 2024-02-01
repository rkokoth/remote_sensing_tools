

import os
import sys
import platform
import time


def gdal_mosaic(path):
    os.chdir(path)
    path = os.getcwd()
    if platform.system() == 'Windows':
        command = f'dir /b /s {path}\*.tif > {path}\list.txt'
    else:
        command = f'ls {path}/*.tif >> {path}/list.txt'
    print(command)
    os.system(command)
    time.sleep(10)
    os.chdir(path)
    os.system(f'gdal_merge.py -o {path}/mosaic.tif --optfile list.txt')
    os.system('rm -fv {path}/list.txt')
if __name__ == '__main__':
    gdal_mosaic(sys.argv[1])
