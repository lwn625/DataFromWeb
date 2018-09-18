import urllib.request
from bs4 import BeautifulSoup
from docx import Document
import re

quote_page='http://ielts.zhan.com/kouyu54286.html'

page=urllib.request.urlopen(quote_page)

soup=BeautifulSoup(page,'html.parser')

file_count=1

for ultag in soup.find_all('td'):
    Tag_a=ultag.find('a')
    if Tag_a is not None:
        child_link=Tag_a['href']
        doc_name_tmp1=Tag_a.text
        # doc_name_tmp2=re.sub(r'[0-9]','',doc_name_tmp1)
        # doc_name_tmp2=re.sub(r'[0-9][0-9]','',doc_name_tmp2)
        # doc_name_tmp2 = re.sub(r'\r\n','',doc_name_tmp2)

        # doc_name_tmp2=doc_name_tmp2.replace('.','')
        # doc_name_tmp2 = doc_name_tmp2.replace('|', '_')
        # doc_name_tmp2 = doc_name_tmp2.replace('?', '')
        doc_name_tmp2 = doc_name_tmp1.replace('/', ' ')

        # print(child_link)
        # print(doc_name_tmp1)
        # print(doc_name_tmp2)
        # print("\n")

        file_count_str=str(file_count)
        file_count_format=file_count_str.zfill(2)
        file_docx=Document()
        name_doc=file_count_format+'_'+doc_name_tmp2+'.docx'
        # print("Output word file is:")
        # print(name_doc)
        # print("\n")
        # #
        child_page=urllib.request.urlopen(child_link)
        child_soup=BeautifulSoup(child_page,'html.parser')
        # print(child_link)
        for child_ultag in child_soup.find_all('div',{'class': 'article-content'}):
            for para in child_ultag.find_all('p'):
                # print(para.text)
                file_docx.add_paragraph(para.text)

        file_docx.save(name_doc)
        file_count = file_count + 1