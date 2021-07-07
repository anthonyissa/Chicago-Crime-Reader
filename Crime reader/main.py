import pandas as pd
import numpy as np
import folium

datas = pd.read_excel('data.xlsx')

listLat = list(datas['Latitude'])
listLong = list(datas['Longitude'])
listDat = list(datas['Date'])
listDesc = list(datas['Description'])
listType = list(datas['Primary Type'])


map = folium.Map(location=[41.8781136, -87.6297982], zoom_start=10)
for x in range(len(listDat)):
    if np.isnan(listLat[x]) or np.isnan(listLong[x]):
        print("rip")
    else:
        folium.Marker([listLat[x], listLong[x]], popup=f"{listDat[x]}\n{listType[x]} {listDesc[x]}").add_to(map)
        print(x)
    if x>=1000:
        break

map.save("map.html")




