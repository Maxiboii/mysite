from map.models import Population, CasesToday, Utility, Map
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv
from math import log, pow


# get population
try:
    url = urllib.request.urlopen('http://database.ukrcensus.gov.ua/PXWEB2007/ukr/news/op_popul.asp')
except:
    url = open('Населення України.html')

soup = BeautifulSoup(url, 'html.parser')


x = soup('table')
a_count = 0
theTable = None
for i in x:
    a_count += 1
    if a_count == 24:
        theTable = i


theData = theTable.contents[9]

population = list()
ff = 1
for number in theData:
    if ff >= 12:
        try:
            region = number.contents[1].text
            if region == 'м.Київ':
                f = region.split('.')
                region = f[0] + '. ' + f[1]
            # else:
            #     region = region + ' область'
            quantity = number.contents[3].text.split(' ')[2]
            x = (region, quantity)
            population.append(x)
        except:
            continue
    ff += 1

# get covid data
url = urllib.request.urlopen('https://moz.gov.ua/article/news/operativna-informacija-pro-poshirennja-koronavirusnoi-infekcii-2019-ncov2')
soup = BeautifulSoup(url, 'html.parser')
x = soup('ul')
a_count = 0
theList = None
for i in x:
    a_count += 1
    if a_count == 3:
        theList = i


todayDate = soup('h4')[0].next_sibling.next_sibling.div.text.strip()
todayCases = soup('h4')[0].parent.next_sibling.next_sibling.div.p.text
todayCases = re.search('\d+\s\d+', todayCases).group(0)


cases = list()
for i in theList:
    try:
        region = re.split('\U00002014', i.text)[0]
        region = re.search('\S+\s\S+', region).group(0)
        if region != 'м. Київ':
            region = region.split()[0]
        quantity = re.split('\U00002014', i.text)[1]
        quantity = re.search('\d+\s\d+|\d+', quantity).group(0)
        try:
            quantity = quantity.replace(' ', '')
        except:
            pass
        x = (region, quantity)
        cases.append(x)
    except:
        continue


population.sort()
cases.sort()


N = 10
indx_lst = list()
for number in range(len(population)):
    regionPopulation = population[number][1]
    casesNumber = cases[number][1]
    indexByregion = round(int(casesNumber)*N/int(regionPopulation), 4)
    if indexByregion > 0.99999:
        print('Scale limit for ' + str(population[number][0]))
        indexByregion = 0.99999
    color = (255*pow(1-indexByregion, 10)*N/10)
    if color > 255:color = 255
    indx_lst.append((indexByregion, color))
for i in indx_lst:
    print(i)


map_data = list()
d = csv.reader(open('map_data.csv', 'r'))
for line in d:
    map_data.append((line[0],line[1]))

map_data.sort()


# for i in range(len(map_data)):
#     print(cases[i][0])
#     print('===')
#     print(map_data[i][0])

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
