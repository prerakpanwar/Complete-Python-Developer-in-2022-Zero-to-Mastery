# import PyPDF2

# pdf_file = "Merged.pdf"
# watermark = "wtr.pdf"
# merged_file = "Watermarked.pdf"

# input_file = open(pdf_file,'rb')
# input_pdf = PyPDF2.PdfFileReader(input_file)
# watermark_file = open(watermark,'rb')
# watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

# pdf_page = input_pdf.getPage(0)
# watermark_page = watermark_pdf.getPage(0)

# pdf_page.mergePage(watermark_page)

# output = PyPDF2.PdfFileWriter()
# output.addPage(pdf_page)

# merged_file = open(merged_file,'wb')
# output.write(merged_file)

# merged_file.close()
# watermark_file.close()
# input_file.close()
        


import PyPDF2

template = PyPDF2.PdfFileReader(open('Merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)