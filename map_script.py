import csv

map_data = list()
d = csv.reader(open('map_data.csv', 'r'))
for line in d:
    map_data.append((line[0],line[1]))

map_data.sort()
for i in map_data:
    print(i[0])
