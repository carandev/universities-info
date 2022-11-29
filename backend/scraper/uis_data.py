import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University


UIS_URL = "https://uis.edu.co"
CAREERS_UIS_URL = f"{UIS_URL}/uis-programas-pregrado-es/"


def get_UIS_data():
    request = requests.get(CAREERS_UIS_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    h4_tags = soup.find_all('h4')

    careers = []

    for tag in h4_tags:
        career_name = tag.get_text()
        career_url = tag.find('a')['href']

        career = Career(name=career_name, page_url=career_url)
        careers.append(career)

    return University(
        name="Universidad Industrial de Santander",
        page_url=UIS_URL,
        careers=careers
    )
