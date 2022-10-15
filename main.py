from pdfminer.high_level import extract_text
from tkinter import *
from PyPDF2 import PdfFileReader

# text1 = extract_text("FIC_Act_Booklet_202012.pdf", "rb")
# print(text)


# root = Tk()
#
# text = Text(root, width=200, height=40)
# text.pack()
#
# text.insert(INSERT, f"{text1}\n")
# text.insert(END, "FishC.com!")
#
# mainloop()

# creating a pdf file object
pdfObject = open('FIC_Act_Booklet_202012.pdf', 'rb')

# creating a pdf reader object
pdfReader = PdfFileReader(pdfObject)

# Extract and concatenate each page's content
text1 = ''
for i in range(0, pdfReader.numPages):
    # creating a page object
    pageObject = pdfReader.getPage(i)
    # extracting text from page
    text1 += pageObject.extractText()
# print(text)

root = Tk()

text = Text(root, width=200, height=40)
text.pack()

text.insert(INSERT, f"{text1}\n")
text.insert(END, "FishC.com!")

mainloop()