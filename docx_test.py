from docx import Document
doc_new=Document()
doc_new.add_paragraph('P1, P2')
doc_new.save('docx_test.docx')
