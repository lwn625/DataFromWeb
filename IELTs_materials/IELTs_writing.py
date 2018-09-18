import urllib.request
from bs4 import BeautifulSoup
from docx import Document

quote_page='http://ielts.zhan.com/xiezuo46991.html'

page=urllib.request.urlopen(quote_page)

soup=BeautifulSoup(page,'html.parser')

file_count=1

for ultag in soup.find_all('td'):
    Tag_a=ultag.find('a')
    if Tag_a is not None:
        child_link=Tag_a['href']
        doc_name=Tag_a.text
        # print(doc_name)

        file_count_str=str(file_count)
        file_count_format=file_count_str.zfill(2)
        file_docx=Document()
        name_doc=file_count_format+'_'+doc_name+'.docx'
        print("Output word file is:")
        print(name_doc)

        child_page=urllib.request.urlopen(child_link)
        child_soup=BeautifulSoup(child_page,'html.parser')
        # print(child_link)
        for child_ultag in child_soup.find_all('div',{'class': 'article-content'}):
            for para in child_ultag.find_all('p'):
                print(para.text)
                file_docx.add_paragraph(para.text)

        file_docx.save(name_doc)
        file_count=file_count+1

    #     link=ultag.find('href')
    #     print(link)
        # print(link.text)
        # print(link.a['href'])
    # print(link)
    # print(ultag.find('a'))
    # print(ultag)
