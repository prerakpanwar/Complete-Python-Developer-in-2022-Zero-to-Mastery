import PyPDF2

with open ('dummy.pdf','rb') as file:       #rb converts file object to binary mode. So, that it can be read.
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
	print(reader.getPage(0))

	page = reader.getPage(0)
	page.rotateCounterClockwise(90)

	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open ('tilted.pdf','wb') as new_file: 
		writer.write(new_file)
