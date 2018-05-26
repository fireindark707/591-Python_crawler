import pickle
import urllib3
import re
import gc
import sys

sys.setrecursionlimit(1000000)  # 递归设置为一百万


def transportation_box():
    MRT = "捷運站"
    TRAIN = "火車站"
    #transportation = [life_box.find(MRT), life_box.find(TRAIN)]
    if life_box.find(MRT) > 0:
        rentDf.ix[num, MRT] = int(1)
    if life_box.find(TRAIN) > 0:
        rentDf.ix[num, TRAIN] = int(1)
    #print(transportation)


condcol = ['押金', '車 位', '管理費', '最短租期', '身份要求', '開伙', '養寵物', '身分要求', '性別要求', '朝向', '格局', '產權登記']
explcol = ['格局', '坪數', '樓層', '型態', '現況', '總樓層數']


rentDf = pickle.load(open("./data/rent_table.dat", "rb"))

http = urllib3.PoolManager()


#url_list = "https://rent.591.com.tw/rent-detail-6396035.html"

#response = http.request('GET', url_list)
#soup = BeautifulSoup(response.data, "lxml")
web_archive_TPE = pickle.load(open("./data/web_archive_5_25_TPE.dat", "rb"))
length = len(web_archive_TPE)
    
for num in range(0, length):
    soup = web_archive_TPE[num]
    
    try:
        price_box = soup.find('div', attrs={'class': 'price clearfix'})
        price_box = price_box.get_text().strip()
        non_decimal = re.compile(r'[^\d.]+')
        price = non_decimal.sub('', price_box)
        rentDf.ix[num, '價格'] = float(price)
        #print(price_box)
    except AttributeError:
        #print("None")
        continue
    
    try:
        explain_box = soup.find('ul', attrs={'class': 'attr'})
        explain = explain_box.findAll('li')
        for item in explain:
            item = item.get_text()
            item_name = item.split('\xa0:\xa0\xa0')[0]
            item_content = item.split('\xa0:\xa0\xa0')[1]
            #print(item)
            if item_name == '坪數':
                item_content = float(item_content.split('坪')[0])
            if item_name == '樓層':
                item_content = item_content.split('/')[0]
                item_content = item_content.split('F')[0]
            if item_name == '總樓層數':
                item_content = item_content.split('/')[1]
                item_content = float(item_content.split('F')[0])
            if item_name in explcol:
                rentDf.ix[num, item_name] = item_content
    
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        address_box = soup.find('span', attrs={'class': 'addr'})
        address_box = address_box.get_text().strip()
        rentDf.ix[num, '地址'] = address_box
        district = address_box.split('區')[0][-2:] + '區'
        rentDf.ix[num, '區'] = district
        #print(address_box)
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        condition_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
        condition = condition_box.findAll('li')
        for item in condition:
            item = item.get_text()
            item_name = item.split('：')[0]
            item_content = item.split('：')[1]
            if item_name == "管理費":
                item_content = non_decimal.sub('', item_content)
                if item_content == "": item_content = 0
            #print(item)
            if item_name in condcol:
                rentDf.ix[num, item_name] = item_content
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
        facility_box = facility_box.find_all('li', class_='clearfix')
        for item in facility_box:
            if 'no' in str(item):
                #print(facility_box[i].get_text(), ": No")
                item = item.get_text()
                rentDf.ix[num, item] = 0
            else:
                #print(facility_box[i].get_text(), ": Yes")
                continue
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        life_box = soup.find('div', attrs={'class': 'lifeBox'})
        life_box = life_box.get_text().strip()
        #print(life_box)
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    transportation_box()
    print(num)
    
    #print(rentDf)
del web_archive_TPE
gc.collect()

web_archive_NTP = pickle.load(open("./data/web_archive_5_25_NTP.dat", "rb"))
length2 = len(web_archive_NTP)
    
for n in range(0, length2):
    soup = web_archive_NTP[n]
    num = n + length
    
    try:
        price_box = soup.find('div', attrs={'class': 'price clearfix'})
        price_box = price_box.get_text().strip()
        non_decimal = re.compile(r'[^\d.]+')
        price = non_decimal.sub('', price_box)
        rentDf.ix[num, '價格'] = float(price)
        #print(price_box)
    except AttributeError:
        #print("None")
        continue
    
    try:
        explain_box = soup.find('ul', attrs={'class': 'attr'})
        explain = explain_box.findAll('li')
        for item in explain:
            item = item.get_text()
            item_name = item.split('\xa0:\xa0\xa0')[0]
            item_content = item.split('\xa0:\xa0\xa0')[1]
            #print(item)
            if item_name == '坪數':
                item_content = float(item_content.split('坪')[0])
            if item_name == '樓層':
                item_content = item_content.split('/')[0]
                item_content = item_content.split('F')[0]
            if item_name == '總樓層數':
                item_content = item_content.split('/')[1]
                item_content = float(item_content.split('F')[0])
            if item_name in explcol:
                rentDf.ix[num, item_name] = item_content
    
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        address_box = soup.find('span', attrs={'class': 'addr'})
        address_box = address_box.get_text().strip()
        rentDf.ix[num, '地址'] = address_box
        district = address_box.split('區')[0][-2:] + '區'
        rentDf.ix[num, '區'] = district
        #print(address_box)
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        condition_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
        condition = condition_box.findAll('li')
        for item in condition:
            item = item.get_text()
            item_name = item.split('：')[0]
            item_content = item.split('：')[1]
            if item_name == "管理費":
                item_content = non_decimal.sub('', item_content)
                if item_content == "": item_content = 0
            #print(item)
            if item_name in condcol:
                rentDf.ix[num, item_name] = item_content
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
        facility_box = facility_box.find_all('li', class_='clearfix')
        for item in facility_box:
            if 'no' in str(item):
                #print(facility_box[i].get_text(), ": No")
                item = item.get_text()
                rentDf.ix[num, item] = 0
            else:
                #print(facility_box[i].get_text(), ": Yes")
                continue
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    try:
        life_box = soup.find('div', attrs={'class': 'lifeBox'})
        life_box = life_box.get_text().strip()
        #print(life_box)
    except AttributeError:
        #print("None")
        continue
    
    #print('\n')
    
    transportation_box()
    print(num)
    
    #print(rentDf)
    
rentDf.to_csv("2018-05-25-TP-result.csv", sep='\t', encoding='utf-8')





