import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv
from math import log, pow


# get population
url = urllib.request.urlopen('http://database.ukrcensus.gov.ua/PXWEB2007/ukr/news/op_popul.asp')

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
url = urllib.request.urlopen('https://moz.gov.ua/article/news/operativna-informacija-pro-poshirennja-koronavirusnoi-infekcii-2019-ncov.')
soup = BeautifulSoup(url, 'html.parser')
x = soup('ul')
a_count = 0
theList = None
for index, i in enumerate(x):
    a_count += 1
    if a_count == 5:
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


info = csv.writer(open('map_info.csv', 'w'))
utility = (todayDate, todayCases, N)
info.writerow(utility)
for line in zip(population, cases, indx_lst):
    info.writerow(line[0])
    info.writerow(line[1])
    info.writerow(line[2])

print('Done')
