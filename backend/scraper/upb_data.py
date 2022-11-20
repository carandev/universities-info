import requests
from bs4 import BeautifulSoup

UPB_URL = "https://www.upb.edu.co/es/pregrados"

request = requests.get(UPB_URL)

soup = BeautifulSoup(request.content, 'html.parser')
div_tags = soup.find_all('li',{'class':'collapsed'})
careers = []

for tag in div_tags:
    career_name = tag.get_text().strip()
    career_url = tag.find('a')['href']

    career = {'name': career_name, 'url': career_url}
    careers.append({
        'name': career_name,
        'url': f'{UPB_URL}{career_url}'
    })

for career in careers:
    print(career)