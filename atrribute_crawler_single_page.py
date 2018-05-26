import pickle
import urllib3
from bs4 import BeautifulSoup
import re


def transportation_box():
    MRT = "捷運站"
    TRAIN = "火車站"
    transportation = [life_box.find(MRT), life_box.find(TRAIN)]
    if life_box.find(MRT) > 0:
        rentDf.ix[0, MRT] = int(1)
    if life_box.find(TRAIN) > 0:
        rentDf.ix[0, TRAIN] = int(1)
    print(transportation)


condcol = ['押金', '車 位', '管理費', '最短租期', '身份要求', '開伙', '養寵物', '身分要求', '性別要求', '朝向', '格局', '產權登記']
explcol = ['格局', '坪數', '樓層', '型態', '現況', '總樓層數']


rentDf = pickle.load(open("./data/rent_table.dat", "rb"))
http = urllib3.PoolManager()
url_list = "https://rent.591.com.tw/rent-detail-6396035.html"
response = http.request('GET', url_list)
soup = BeautifulSoup(response.data, "lxml")

print("------------------------Seperator-----------------------------")

try:
    price_box = soup.find('div', attrs={'class': 'price clearfix'})
    price_box = price_box.get_text().strip()
    non_decimal = re.compile(r'[^\d.]+')
    price = non_decimal.sub('', price_box)
    rentDf.ix[0, '價格'] = float(price)
    print(price_box)
except AttributeError:
    print("None")
print('\n')

try:
    explain_box = soup.find('ul', attrs={'class': 'attr'})
    explain = explain_box.findAll('li')
    for item in explain:
        item = item.get_text()
        item_name = item.split('\xa0:\xa0\xa0')[0]
        item_content = item.split('\xa0:\xa0\xa0')[1]
        print(item)
        if item_name == '坪數':
            item_content = float(item_content.split('坪')[0])
        if item_name == '樓層':
            item_content = item_content.split('/')[0]
            item_content = item_content.split('F')[0]
        if item_name == '總樓層數':
            item_content = item_content.split('/')[1]
            item_content = float(item_content.split('F')[0])
        if item_name in explcol:
            rentDf.ix[0, item_name] = item_content
except AttributeError:
    print("None")
print('\n')

try:
    address_box = soup.find('span', attrs={'class': 'addr'})
    address_box = address_box.get_text().strip()
    rentDf.ix[0, '地址'] = address_box
    district = address_box.split('區')[0][-2:] + '區'
    rentDf.ix[0, '區'] = district
    print(address_box)
except AttributeError:
    print("None")
print('\n')

try:
    condition_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
    condition = condition_box.findAll('li')
    for item in condition:
        item = item.get_text()
        item_name = item.split('：')[0]
        item_content = item.split('：')[1]
        print(item)
        if item_name in condcol:
            rentDf.ix[0, item_name] = item_content
except AttributeError:
    print("None")
print('\n')

try:
    facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
    facility_box = facility_box.find_all('li', class_='clearfix')
    for i in range(0, len(facility_box)):
        if 'no' in str(facility_box[i]):
            print(facility_box[i].get_text(), ": No")
            rentDf.ix[0, facility_box[i]] = 0
        else:
            print(facility_box[i].get_text(), ": Yes")
except AttributeError:
    print("None")
print('\n')

try:
    life_box = soup.find('div', attrs={'class': 'lifeBox'})
    life_box = life_box.get_text().strip()
    print(life_box)
except AttributeError:
    print("None")
print('\n')

transportation_box()
print(rentDf)
