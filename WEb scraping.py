import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48"
response = requests.get(base_url)

soup = BeautifulSoup(response.content, 'lxml')
csv_file = open('test.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['PRODUCT DETAIL','COMPANY','PRICE', 'SHIPPING'])

for table in soup.find_all('div',class_='item-container'):
    
    detail = table.find('a', class_="item-title").text
    
    for title in soup.find_all('div', class_="item-branding"):
        company = title.find('img').get('title')
        
    price = table.find('li', class_="price-current").text
    shipping = table.find('li', class_="price-ship").text
    
    csv_writer.writerow([detail, company, price, shipping])
    
csv_file.close()