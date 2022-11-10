import requests
from bs4 import BeautifulSoup

UIS_URL = "https://uis.edu.co/uis-programas-pregrado-es/"

request = requests.get(UIS_URL)

soup = BeautifulSoup(request.content, 'html.parser')
h4_tags = soup.find_all('h4')

careers = []

for tag in h4_tags:
    career_name = tag.get_text()
    career_url = tag.find('a')['href']

    career = {'name': career_name, 'url': career_url}
    careers.append(career)

for career in careers:
    print(career)
