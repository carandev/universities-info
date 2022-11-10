import requests
from bs4 import BeautifulSoup

UDES_URL = "https://bucaramanga.udes.edu.co/estudia/pregrados"

request = requests.get(UDES_URL)

soup = BeautifulSoup(request.content, 'html.parser')
tr_tags = soup.find_all('tr')

careers = []

for tag in tr_tags[1:]:
    career_name = tag.find('a').get_text()
    career_url = tag.find('a')['href']

    careers.append({
        'name': career_name,
        'url': f'{UDES_URL}{career_url}'
    })

for career in careers:
    print(career)
