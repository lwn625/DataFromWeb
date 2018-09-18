import requests
from bs4 import BeautifulSoup

# Load the webpage url
r = requests.get("https://mp.weixin.qq.com/s/tzFKo2e3FM-TEpPjGuhPaQ")

# Use beautifulSoup to parse the webpage
bs = BeautifulSoup(r.text,'lxml')

# Index number for output image name
i=1

# The assumption is to find all img tags in the webpage
# Of course it will contain some files that we do not need
# but Considerring the numebr of unwanted image files is relativly small
# So we could go ahead with this simple selection
for link in bs.find_all('img'):
    # Find the real real source of the image file
    # Sometimes, the format could be: src= rather than data-src=
    # It is necessary to go to the page source to verify
    image=link.get("data-src")
    # print the found image sources, and check
    # print(image)

    # in this case, some img tags do not provide a valid image source
    # so there are some None output of print(image)
    # So use if to only consider valid image sources_
    if image is not None:
        # Name the downloaded images files as: 01, 02, 03....
        img_name_index = str(i).zfill(2)
        img_name = img_name_index + '.jpg'
        # use request.get to download the image
        # and write into the current folder
        r2 = requests.get(image)
        with open(img_name, "wb") as f:
            f.write(r2.content)
        i=i+1
