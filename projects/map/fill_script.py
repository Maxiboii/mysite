from map.models import Population, CasesToday, Utility, Map
import csv


population = list()
cases = list()
indx_lst = list()
info = csv.reader(open('map_info.csv', 'r'))
for index, line in enumerate(info):
    if index == 0:
        todayDate = line[0]
        todayCases = line[1]
        N = line[2]
    else:
        if index % 3 == 1:
            population.append(line)
        elif index % 3 == 2:
            cases.append(line)
        else:
            indx_lst.append(line)


map_data = list()
d = csv.reader(open('map_data.csv', 'r'))
for line in d:
    map_data.append((line[0],line[1]))

map_data.sort()


# emptying
Population.objects.all().delete()
CasesToday.objects.all().delete()
Map.objects.all().delete()
Utility.objects.all().delete()


print('Filling the Databse')

for row in range(len(population)):
    print(row)
    p, created = Population.objects.get_or_create(region=population[row][0],
    population=population[row][1]
    )
    m_d, created = Map.objects.get_or_create(data=map_data[row][1])
    c_d, created = CasesToday.objects.get_or_create(cases=cases[row][1],
    indx=indx_lst[row][0],color=indx_lst[row][1]
    )
    c_d.region_id = p.id
    c_d.save()
    m_d.region_id = p.id
    m_d.cases_id = c_d.id
    m_d.save()


ut_d, created = Utility.objects.get_or_create(title='date',value=todayDate)
ut_c, created = Utility.objects.get_or_create(title='cases',value=todayCases)
ut_n, created = Utility.objects.get_or_create(title='N',value=N)

print('Database filled')
