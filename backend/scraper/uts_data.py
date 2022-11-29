import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University


UTS_URL = "https://www.uts.edu.co"
CAREER_UTS_URL = f"{UTS_URL}/sitio/oferta-academica-2/"


def get_UTS_data():
    request = requests.get(CAREER_UTS_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    tr_tags = soup.find_all('tr')

    careers = []

    for tag in tr_tags:

        a_tags = tag.find_all('a')

        if len(a_tags) != 0:
            career_name = a_tags[-1].get_text()
            career_url = a_tags[-1]['href']

            careers.append(Career(
                name=career_name,
                page_url=career_url
            ))

    return University(
        name="Unidades Tecnológicas de Santander",
        page_url=UTS_URL,
        careers=careers
    )
