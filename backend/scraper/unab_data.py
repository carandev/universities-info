import requests
from bs4 import BeautifulSoup

UNAB_URL = "https://unab.edu.co/pregrados/"

request = requests.get(UNAB_URL)

soup = BeautifulSoup(request.content, 'html.parser')
h2_tags = soup.find_all('h2')

careers = []

for tag in h2_tags[:-13]:
    career_name = tag.get_text().strip()
    career_url = tag.find('a')['href']

    career = {'name': career_name, 'url': career_url}
    careers.append(career)

for career in careers:
    print(career) 
