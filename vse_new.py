import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml


url = 'https://www.vseinstrumenti.ru/brand/lezard-13097/page3/#searchQuery=lezard&searchType=redirect'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')

soup = block.find('div', class_='_1z2cuE G-rflf').find_all('div', class_='Wk5Je9 LXySrk')
print(len(block))
# for i in block:
#     w = i.find_next('div', class_='Z6EojR Z9UMXC').find('a').get('href')
#     print(w)
