from PyPDF2 import PdfFileReader
from pathlib import Path
import pandas as pd
import numpy as np

pdf = PdfFileReader('SAD.pdf')

my_dict = {"Requirement":[],"Details":[]}


#create a text file of the pdf to extract data
with Path('SAD.txt').open(mode='w') as output_file:
    text = ''
    for page in pdf.pages:
        text += page.extractText()
    output_file.write(text)

with open('SAD.txt','r') as sad:
    for line in sad:
        if 'STTSRS' in line:
            data = line.strip().split(':')
            my_dict['Requirement'].append(data[0])
            my_dict['Details'].append(data[1])


df = pd.DataFrame(my_dict)

#setting count to 1
df.index = np.arange(1, len(df)+1)


#save as csv
df.to_csv('requirements_list.csv', index_label='#') 



