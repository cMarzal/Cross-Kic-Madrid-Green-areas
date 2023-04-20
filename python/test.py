import pandas as pd
import geopandas
from read_shapeFile import loadShapeFile

nums = []
huerto = pd.DataFrame([])
zona = pd.DataFrame([])
patio = pd.DataFrame([])

for i in range(21):
    if i < 10:
        nums.append('D0'+str(i+1))
    else:
        nums.append('D' + str(i + 1))
print('Creating green spaces from all the census areas')
for folder in nums:
    try:
        urbanGardens_shp = loadShapeFile('data/carto2/' + folder + '/11_HUERTO_URBANO_P.shp')
        huerto = pd.concat([huerto, urbanGardens_shp])
    except:
        is_green = 0

    try:
        gardenAreas_shp = loadShapeFile('data/carto2/' + folder + '/11_ZONA_AJARDINADA_P.shp')
        zona = pd.concat([zona, gardenAreas_shp])
    except:
        is_green = 0

    try:
        gardenInPatios_shp = loadShapeFile('data/carto2/' + folder + '/11_ZONA_AJARDINADA_SOBRE_PATIO_P.shp')
        patio = pd.concat([patio, gardenInPatios_shp])
    except:
        is_green = 0


huerto.to_file('out/test/huerto.shp', driver='ESRI Shapefile')
zona.to_file('out/test/zona.shp', driver='ESRI Shapefile')
patio.to_file('out/test/patio.shp', driver='ESRI Shapefile')
