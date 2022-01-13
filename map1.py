import folium
import pandas 
data=pandas.read_csv("Volcanoes.txt")
lon=list(data["LON"])
lat=list(data["LAT"])
elev=list(data["ELEV"])
map1=folium.Map(location=[26.00,30.75],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="Volacanoes")

def color_producer(elevation):
    if elevation<1000:
      return 'green'
    elif 1000<=elevation <1500:
        return 'orange'
    elif 1500<=elevation<2000:
        return 'red'
    elif 2000<=elevation<3000:
        return 'blue'
    else:
        return 'purple'
for lt,ln,el in zip(lat,lon,elev):
 fg.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+"m",radius=5,fill_color=color_producer(el),color='grey',fill_opacity=0.7 ))

fp=folium.FeatureGroup(name="Population")

fp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green'if x['properties']['POP2005']< 10000000 
else 'orange ' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map1.add_child(fp)
map1.add_child(fg)
map1.add_child(folium.LayerControl())
map1.save("Map5.html")
