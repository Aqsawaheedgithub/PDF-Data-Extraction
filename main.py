# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('python.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))

# creating a page object
pageObj = pdfReader.pages[0]
pageObj = pdfReader.pages[1]
pageObj = pdfReader.pages[2]
pageObj = pdfReader.pages[3]
pageObj = pdfReader.pages[4]
pageObj = pdfReader.pages[5]
pageObj = pdfReader.pages[6]
pageObj = pdfReader.pages[7]
pageObj = pdfReader.pages[8]
pageObj = pdfReader.pages[9]
pageObj = pdfReader.pages[10]
pageObj = pdfReader.pages[11]
pageObj = pdfReader.pages[12]
pageObj = pdfReader.pages[13]
pageObj = pdfReader.pages[14]
pageObj = pdfReader.pages[15]
pageObj = pdfReader.pages[16]
pageObj = pdfReader.pages[17]
pageObj = pdfReader.pages[18]
pageObj = pdfReader.pages[19]
pageObj = pdfReader.pages[20]
pageObj = pdfReader.pages[21]
pageObj = pdfReader.pages[22]
pageObj = pdfReader.pages[23]
pageObj = pdfReader.pages[24]
pageObj = pdfReader.pages[25]
pageObj = pdfReader.pages[26]
pageObj = pdfReader.pages[28]
# extracting text from page
print(pageObj.extract_text())

# closing the pdf file object
pdfFileObj.close()