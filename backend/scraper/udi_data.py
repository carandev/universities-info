import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University

UDI_URL = "https://www.udi.edu.co"
CAREER_UDI_URL = f"{UDI_URL}/programas"


def get_UDI_data():
    request = requests.get(CAREER_UDI_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    span_tags = soup.find_all('li', {'class': 'div-carrera'})
    careers = []

    for tag in span_tags:
        career_name = tag.get_text().strip()
        career_url = tag.find('a')['href']

        careers.append(Career(
            name=career_name,
            page_url=f'{CAREER_UDI_URL}{career_url}'
        ))

    return University(
        name="Universidad de Investigación y Desarrollo",
        page_url=UDI_URL,
        careers=careers
    )
