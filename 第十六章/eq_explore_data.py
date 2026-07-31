#-------------------------------------------------------------------------------
###16.2.2查看GeoJSON数据
from pathlib import Path
import json

#将数据作为字符串读取并转换为 Python 对象
path = Path(r'D:\代码\PY_test\第十六章\geojson\eq_data_1_day_m1.geojson')
connects = path.read_text()
all_eq_data = json.loads(connects)     #将connects转换成字典的形式
#print(all_eq_data)

#将数据文件转换为更易读的版本
path = Path(r'D:\代码\PY_test\第十六章\geojson\readable_eq_data.geojson')
readable_connects = json.dumps(all_eq_data, indent = 4)
path.write_text(readable_connects)

#-------------------------------------------------------------------------------
###16.2.3创建地震列表
all_eq_dicts = all_eq_data['features']          #取的是features这个key对应的value
print(len(all_eq_dicts))                        #计算这个value的长度

path = Path(r'D:\代码\PY_test\第十六章\geojson\features.json')     #保存字典，可以看里面什么样
path.write_text(json.dumps(all_eq_dicts, indent=4))

#-------------------------------------------------------------------------------
###16.2.4提取震级
#mags = []
#for eq_dict in all_eq_dicts:
#    mag = eq_dict['properties']['mag']
#    mags.append(mag)

#print(mags[:10])


#-------------------------------------------------------------------------------
###16.2.5提取位置数据
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

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

#-------------------------------------------------------------------------------
###16.2.6绘制散点图
#import plotly.express as px

#fig = px.scatter(
#    x = lons,
#    y = lats,
#    labels = {'x':'经度', 'y': '纬度'},
#    range_x = [-200, 200],
#    range_y = [-90, 90],
#    width = 800,
#    height = 800,
#    title = '全球地震散点图'
#)
#fig.write_html(r'D:\代码\PY_test\第十六章\html\global_earthquakes.html')
##fig.show()

#-------------------------------------------------------------------------------
###16.2.7指定数据的另一种形式
import plotly.express as px
import pandas as pd

data = pd.DataFrame(
    data = zip(lons, lats, titles, mags), columns = ['经度', '纬度', '位置', 
    '震级']
)
data.head()

#fig = px.scatter(
#    data,
#    x = '经度',
#    y = '纬度',
#    range_x = [-200, 200],
#    range_y = [-90, 90],
#    width = 800,
#    height = 800,
#    title = '全球地震散点图'
#
#fig.write_html(r'D:\代码\PY_test\第十六章\html\global_earthquakes.html')
##fig.show()


#-------------------------------------------------------------------------------
###16.2.8定制标记尺寸
fig = px.scatter(
    data,
    x = '经度',
    y = '纬度',
    range_x = [-200, 200],
    range_y = [-90, 90],
    width = 800,
    height = 800,
    title = '全球地震散点图',
    size = '震级',
    size_max = 10,                    #根据震级的大小改变散点图中点的大小
)
fig.write_html(r'D:\代码\PY_test\第十六章\html\global_earthquakes.html')
#fig.show()

#-------------------------------------------------------------------------------


































