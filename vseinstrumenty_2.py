import bs4
import time
import csv
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

count = 1
while count <= 60:

    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(
            f"https://www.vseinstrumenti.ru/brand/lezard-13097/page{count}/#searchQuery=lezard&searchType=redirect")  # Открываем страницу
        time.sleep(3)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        block = soup.find('div', class_='_1z2cuE').find_all('div', class_='dGMJLz fSNq2j Ppy5qY LXySrk')
        print(len(block))
        for i in block:
            w = i.find_next('div', class_='Z6EojR Z9UMXC').find('a').get('href')
            print(w)
            with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options) as driver:  # Открываем хром
                driver.get(w)  # Открываем страницу
                time.sleep(3)  # Время на прогрузку страницы
                loom = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                name = loom.find('div', class_='pKTE7p').find('h1')
                print(name.text.strip())
                head = (name.text.strip())
                price = loom.find('div', class_='df5X3i')
                print(price.text.strip())
                cena = (price.text.strip())
                codd = loom.find('div', class_='c8-E0f').find('span')
                print(codd.text.strip())
                art = (codd.text.strip())
                pixes = loom.find('div', class_='content').find_all('a', href=True)
                # print(len(pixes))
                img = []
                for pix in pixes:
                    print(pix['href'])
                    foto = (pix['href'])
                    img.append(foto)
                params = loom.find('div', class_='_6fLeAS').find_all('p')
                value = []
                for param in params:
                    print(param.text.strip())
                    charact = (param.text.strip())
                    value.append(charact)
                print('\n')

                # storage = {'name': head, 'price': cena, 'code': art, 'params': '; '.join(value), 'photo': '$'.join(img),
                #            'URL': w}
                # with open('example.csv', 'a+', encoding='utf-16') as file:
                #     pisar = csv.writer(file, delimiter='$', lineterminator='\r')
                #     pisar.writerow(
                #         [storage['name'], storage['price'], storage['code'], storage['params'], storage['photo'],
                #          storage['URL']])
        count += 1
        print(count)
