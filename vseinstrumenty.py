import bs4
import time
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) as driver:  # Открываем хром
    driver.get("https://www.vseinstrumenti.ru/brand/lezard-13097/page3/#searchQuery=lezard&searchType=redirect")  # Открываем страницу
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
            price = loom.find('div', class_='df5X3i')
            print(price.text.strip())
            codd = loom.find('div', class_='c8-E0f').find('span')
            print(codd.text.strip())
            pixes = loom.find('div', class_='content').find_all('a', href=True)
            # print(len(pixes))
            for pix in pixes:
                print(pix['href'])
            params = loom.find('div', class_='_6fLeAS').find_all('p')
            for param in params:
                print(param.text.strip())
            print('\n')
