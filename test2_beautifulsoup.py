import urllib.request
from bs4 import BeautifulSoup
import csv
# quote_page='http://www.bloomberg.com/quote/SPX:IND'
# page=urllib.request.urlopen(quote_page)
#
# soup=BeautifulSoup(page,'html.parser')
#
# name_box=soup.find('h1',attrs={'class': 'name'})
# name=name_box.text.strip()
# print(name)

quote_page='https://organicfoodsandcafe.com/product-category/baby/baby-baby/food/'
# quote_page='https://organicfoodsandcafe.com/product-category/baby/baby-baby/food/page/3/'
page=urllib.request.urlopen(quote_page)

filename='Baby_Food_Price.csv'

soup=BeautifulSoup(page,'html.parser')

name=[]
price_num=[]
price_currency=[]

name_count=1
price_count=1

# for headers in soup.find_all('h3'):
for ultag in soup.find_all('ul',{'class': 'products'}):
    for headers in ultag.find_all('h3'):
        name.append(headers.text.strip())
        name_count=name_count+1

    for price in ultag.find_all('span',attrs={'class': 'woocommerce-Price-amount amount'}):
        price_style=price.text.strip()
        price_style_split=price_style.split()
        price_num.append(price_style_split[1])
        price_currency.append(price_style_split[0])
        price_count=price_count+1
# print(name)
print(price_num)
print(price_currency)


if name_count==price_count:
    rows_zip = zip(name, price_num, price_currency)
    with open(filename,'w',newline='') as f:
        writer=csv.writer(f)
        for row in rows_zip:
            writer.writerow(row)

f.close()


# print(name_count)
# print(price_count)