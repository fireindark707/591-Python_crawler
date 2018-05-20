import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url_list = "https://rent.591.com.tw/rent-detail-6308664.html"

response = http.request('GET', url_list)
soup = BeautifulSoup(response.data, "lxml")

price_box = soup.find('div', attrs={'class': 'price clearfix'})
price_box = price_box.get_text()

explain_box = soup.find('ul', attrs={'class': 'attr'})
explain_box = explain_box.get_text()

address_box = soup.find('span', attrs={'class': 'addr'})
address_box = address_box.get_text()

condition_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
condition_box = condition_box.get_text()

facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
facility_box = facility_box.find_all('li', class_='clearfix')


print("--------------------------------------------------------")
print(price_box)
print(explain_box)
print(address_box)
print(condition_box)

for i in range(0, len(facility_box)):
    # a = "<span class=\"no\">"
    if 'no' in str(facility_box[i]):
        print(facility_box[i])
    else:
        print(i)
