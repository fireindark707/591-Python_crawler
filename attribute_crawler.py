import urllib3
import pickle
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url_list = pickle.load(open("./data/url_list_5_20.dat", "rb"))

length = len(url_list)

for i in range(0, length):
    response = http.request('GET', url_list[i])
    soup = BeautifulSoup(response.data, "lxml")

    price_box = soup.find('div', attrs={'class': 'price clearfix'})
    price_box = price_box.get_text()

    explain_box = soup.find('ul', attrs={'class': 'attr'})
    explain_box = explain_box.get_text()

    address_box = soup.find('span', attrs={'class': 'addr'})
    address_box = address_box.get_text()

    condtion_box = soup.find('ul', attrs={'class': 'clearfix labelList labelList-1'})
    condtion_box = condtion_box.get_text()

    facility_box = soup.find('ul', attrs={'class': 'facility clearfix'})
    facility_box = facility_box.get_text()

    print("--------------------------------------------------------")
    print(price_box)
    print(explain_box)
    print(address_box)
    print(condtion_box)
    print(facility_box)
