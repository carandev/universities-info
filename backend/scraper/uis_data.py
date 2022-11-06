import requests
from bs4 import BeautifulSoup

UIS_URL = "https://uis.edu.co/uis-programas-pregrado-es/"

request = requests.get(UIS_URL)

soup = BeautifulSoup(request.content, 'html.parser')
h4_tags = soup.find_all('h4')

for tag in h4_tags:
    carer_name = tag.get_text()
    carer_url = tag.find('a')['href']

    carer = {'name': carer_name, 'url': carer_url}
