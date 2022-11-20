import requests
from bs4 import BeautifulSoup

UTS_URL = "https://www.uts.edu.co/sitio/oferta-academica-2/"

request = requests.get(UTS_URL)

soup = BeautifulSoup(request.content, 'html.parser')
tr_tags = soup.find_all('tr')

careers = []

for tag in tr_tags:

    a_tags = tag.find_all('a')

    if len(a_tags) != 0:
        career_name = a_tags[-1].get_text()
        career_url = a_tags[-1]['href']
        
        careers.append({
            'name': career_name,
            'url': career_url
        })

for career in careers:
    print(career)

