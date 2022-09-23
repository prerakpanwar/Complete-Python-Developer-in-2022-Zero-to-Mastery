# import PyPDF2
  
# # creating a pdf file object
# pdfFileObj = open('twopage.pdf', 'rb')
  
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# # printing number of pages in pdf file
# print(pdfReader.numPages)
  
# # creating a page object
# pageObj = pdfReader.getPage(0)
  
# # extracting text from page
# print(pageObj.extractText())
  
# # closing the pdf file object
# pdfFileObj.close()


import PyPDF2
with open('twopage.pdf','rb') as pdf_file, open('twopage_text.txt', 'w') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   # use xrange in Py2
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)