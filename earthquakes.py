import urllib
import json
import pandas as pd

url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
d = json.loads(urllib.urlopen(url).read())

data = pd.DataFrame(d.items())

data

data[1][1][0]

earthquakes = []

for fields in data[1][1]:

    src = fields['properties']['net']
    eqid = fields['properties']['code']
    datetime = fields['properties']['time']
    lon = fields['geometry']['coordinates'][0]
    lat = fields['geometry']['coordinates'][1]
    mag = fields['properties']['mag']
    depth = fields['geometry']['coordinates'][2]
    nst = fields['properties']['nst']
    place = fields['properties']['place']
    
    earthquake = []
    earthquake.append(src)
    earthquake.append(eqid)
    earthquake.append(datetime)
    earthquake.append(lat)
    earthquake.append(lon)
    earthquake.append(mag)
    earthquake.append(depth)
    earthquake.append(nst)
    earthquake.append(place)
    earthquakes.append(earthquake)

df = pd.DataFrame(np.array(earthquakes), columns = ['Src','Eqid','Datetime','Lat','Lon','Mag','Depth','Nst','Place'])
df[0:10]

California = df[df.Src == 'ci']
california[0:5]
print california.Lon[0:5]
california.Lat[0:5]

from mpl_toolkits.basemap import Basemap

def plot_quakes(quakes):
    m = Basemap(llcrnrlon=-124.960938,llcrnrlat=41.956070,
                urcrnrlon=-114.062500,urcrnrlat=32.236792,
                resolution='l',area_thresh=1000.,projection='merc',
                lat_0=37.147894,lon_0=-119.599609)
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='coral',lake_color='blue')
    m.drawmapboundary(fill_color='aqua')
    x, y = m(quakes.Lon, quakes.Lat)
    m.plot(x, y, 'k.')
    return m

plot_quakes(california)
