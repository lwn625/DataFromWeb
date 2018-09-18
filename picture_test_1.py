# import urllib.request
# import os
# import re
#
# def url_open(url):
#     req=urllib.request.Request(url)
#     req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
#     response=urllib.request.urlopen(req)
#     return response.read()
#
# def get_page(url):
#     html=url_open(url).decode('utf-8')
#     pattern=

import requests
from bs4 import BeautifulSoup

# r = requests.get("http://www.pythonscraping.com")
# bs = BeautifulSoup(r.text,'lxml')
# image = bs.find("a", {"id": "logo"}).find("img")["src"]
#
# ir = requests.get(image)
# if ir.status_code == 200:
#     open('logo.jpg', 'wb').write(ir.content)


r = requests.get("http://www.luluwebstore.com/products/lulu-food-cupboard-baby-baby-food/milupa/aptamil-pronutra-1-infant-formula-900g/pid-8242852.aspx")
bs = BeautifulSoup(r.text,'lxml')
image = bs.find("a", {"id": "divImgContainer"}).find("img")["src"]

ir = requests.get(image)
if ir.status_code == 200:
    open('test.jpg', 'wb').write(ir.content)