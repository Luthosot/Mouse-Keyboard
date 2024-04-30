'Web scraping '
import requests
from bs4 import BeautifulSoup
import requests
URL = 'https://steers2023.pages.dev/images/promos/2024/april/yavaya/yavaya-homepage-promo.png'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify())

product_title = soup.find(class_='product_title').get_text()
product_price = soup.find(class_='display_price').get_text()

print(product_title)
print(product_price)

      