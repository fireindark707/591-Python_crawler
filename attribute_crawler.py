import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = "https://rent.591.com.tw/rent-detail-6308664.html"

response = http.request('GET', url)
soup = BeautifulSoup(response.data, "lxml")

price_box = soup.find('div', attrs={'class': 'price clearfix'})
price_box = price_box.i
price_box.b.unwrap()
# price = price_box.string.extract()

explain_box = soup.find('ul', attrs={'class': 'attr'})
# explain_box = explain_box.li

address_box = soup.find('span', attrs={'class': 'addr'})

condtion_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})

facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})

print("--------------------------------------------------------")
print(price_box)
print(explain_box)
print(address_box)
print(condtion_box)
print(facility_box)
