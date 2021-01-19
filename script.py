
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'satellite_colletion.settings')

django.setup()

from os import walk
from django.contrib.gis.gdal import GDALRaster
from main.models import Test8
import subprocess
import geemap
import ee


file_path = r"D:\Geodjango_env\satellite_colletion\rasters"
# print(file_path)
try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

loc = ee.Geometry.Point(-99.2222, 46.7816)
collection = ee.ImageCollection('USDA/NAIP/DOQQ') \
    .filterBounds(loc) \
    .filterDate('2008-01-01', '2020-01-01') \
    .filter(ee.Filter.listContains("system:band_names", "N"))


out_dir = r"D:\Geodjango_env\satellite_colletion\rasters"
geemap.ee_export_image_collection(collection, out_dir=out_dir)


# from elevation.models import Elevation
#     dem = Test2(name='Volcano', rast='/path/to/raster/volcano.tif')
#     dem.save()

for root, dirs, files in os.walk(file_path):

    for raster in files:
        if raster.endswith(".tif"):
            # collection_list = collection.toList(collection.size())
            # n = collection.size().getInfo()
            # for i in range(0, n, 1):
            #     img = ee.Image(collection_list.get(i))
            #     img_dict = img.getInfo()
            #     name = img_dict.get("id")
            raster_path=os.path.join(root, raster)
            raster = GDALRaster( raster_path,write=True)
            dem = Test8(raster=raster)
            dem.save()






# collection_list = collection.toList(collection.size())
            # n = collection.size().getInfo()
            # for i in range(0, n, 1):
            #     img = ee.Image(collection_list.get(i))
            #     img_dict = img.getInfo()
            #     name = img_dict.get("id")