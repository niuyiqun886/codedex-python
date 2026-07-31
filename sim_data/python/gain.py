from pathlib import Path
import csv

path = Path(r'D:\代码\PY_test\sim_data\sim_csv\gain.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index,column in enumerate(header_row):
    print(index,column)


rows = list(reader)
time = [float(row[0]) for row in rows]

print(time)











