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
###提取震级
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags)

