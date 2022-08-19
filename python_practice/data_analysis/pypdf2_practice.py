from operator import imod
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import re

pdf = PdfFileReader('data_analysis/lorem.pdf')

#grab page 1
page_1_object = pdf.getPage(0)
#print(page_1_object)

#/StructParents shows the page index

#Extract the text
page_1_text = page_1_object.extract_text()
#print(page_1_text)

#Combine the text from all pages and save as text file
with Path('data_analysis/lorem_text.txt').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)

#Where's waldo?
waldo_pages = []

for page in pdf.pages:
    page_num = page['/StructParents']
    page_text = page.extractText()

    if 'Waldo' in page_text:
        waldo_pages.append(page_num)

print(waldo_pages)

#saves pages to a pdf
input_pdf = PdfFileReader('data_analysis/lorem.pdf')

output_pdf = PdfFileWriter()


for page in waldo_pages:
    page_object = input_pdf.getPage(page)
    output_pdf.addPage(page_object)

#save to pdf
with Path('data_analysis/waldo_pages.pdf').open(mode='wb') as output_file_2:
    output_pdf.write(output_file_2)

page_sentences = []
for page in pdf.pages:
    page_num = page['/StructParents']
    page_text = page.extractText()

    if 'Waldo' in page_text:
        
        #use re to seperate out texts with Waldo
        sentence_list = ['page' + str(page_num) + ':' + sentence.replace('\n', '') for sentence in re.split('\. |\? |\!', page_text) if 'Waldo' in sentence][0]
        page_sentences.append(sentence_list)

text = '\n'.join(page_sentences)

with Path('data_analysis/waldo_sentences_pages.text').open(mode='w') as output_file_3:
    output_file_3.write(text)