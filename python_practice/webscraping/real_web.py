from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.ziprecruiter.com/candidate/search?form=jobs-landing&search=python&location=Arlington+Heights%2C+IL').text
soup = BeautifulSoup(html_text, 'lxml')
find = soup.find('a',class_= 'job_link t_job_link')
print(find)

