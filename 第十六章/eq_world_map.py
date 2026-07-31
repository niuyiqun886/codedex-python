#-------------------------------------------------------------------------------
###16.2.9定制标记的颜色
from pathlib import Path
import json
import plotly.express as px
import pandas as pd

path= Path(r'D:\代码\PY_test\第十六章\geojson\eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding = 'utf-8')


all_eq_data = json.loads(contents)
path = Path(r'D:\代码\PY_test\第十六章\geojson\readable_eq_data.geojson')
readable_connects_1 = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_connects_1)

all_eq_dicts = all_eq_data['features']          #取的是features这个key对应的value
print(len(all_eq_dicts))                        #计算这个value的长度

#标题变为表中标题
title_name = all_eq_data['metadata']['title']
print(title_name)

#保存字典
path = Path(r'D:\代码\PY_test\第十六章\geojson\features_1.json')     #保存字典，可以看里面什么样
path.write_text(json.dumps(all_eq_dicts, indent=4))

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data = zip(lons, lats, titles, mags), columns = ['经度', '纬度', '位置', 
    '震级']
)
data.head()

fig = px.scatter(
    data,
    x = '经度',
    y = '纬度',
    range_x = [-200, 200],
    range_y = [-90, 90],
    width = 800,
    height = 800,
    title = title_name,
    size = '震级',
    size_max = 10,                    #根据震级的大小改变散点图中点的大小
    color = '震级',
    hover_name = '位置'
)
fig.write_html(r'D:\代码\PY_test\第十六章\html\global_earthquakes_1.html')
#fig.show()


















