import requests
from bs4 import BeautifulSoup

UDI_URL = "https://www.udi.edu.co/programas"

request = requests.get(UDI_URL)

soup = BeautifulSoup(request.content, 'html.parser')
span_tags = soup.find_all('li', {'class':'div-carrera'})
careers = []

for tag in span_tags:
    career_name = tag.get_text().strip()
    career_url = tag.find('a')['href']

    #carer = {'name': career_name, 'url': career_url}
    careers.append({
        'name': career_name,
        'url': f'{UDI_URL}{career_url}'
    })

for career in careers:
    print(career)