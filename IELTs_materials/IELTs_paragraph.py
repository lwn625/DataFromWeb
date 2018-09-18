import urllib.request
from bs4 import BeautifulSoup
from docx import Document
quote_page='http://ielts.zhan.com/xiezuo59538.html'

page=urllib.request.urlopen(quote_page)
file_doc=Document()
soup=BeautifulSoup(page,'html.parser')
file_count=1
for ultag in soup.find_all('div',{'class': 'article-content'}):
    # para=ultag.find_all('p')
    # print(para[0].text)

    for para in ultag.find_all('p'):
        file_doc.add_paragraph(para.text)

      # print(para.text)
file_doc.save('para_test.docx')