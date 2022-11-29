import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University

UPB_URL = "https://www.upb.edu.co/es"
CAREERS_UPB_URL = f"{UPB_URL}/pregrados"


def get_UPB_data():
    request = requests.get(CAREERS_UPB_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    div_tags = soup.find_all('li', {'class': 'collapsed'})
    careers = []

    for tag in div_tags:
        career_name = tag.find("div", {"class": "texto"}).get_text()
        career_url = tag.find('a')['href']

        careers.append(Career(
            name=career_name,
            page_url=f'{CAREERS_UPB_URL}{career_url}'
        ))

    return University(
        name="Universidad Pontificia Bolivariana",
        page_url=UPB_URL,
        careers=careers
    )
