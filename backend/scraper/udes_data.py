import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University

UDES_BASE_URL = "https://bucaramanga.udes.edu.co"
CAREERS_URL = f"{UDES_BASE_URL}/estudia/pregrados"


def get_UDES_data():
    request = requests.get(CAREERS_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    tr_tags = soup.find_all('tr')

    careers = []

    for tag in tr_tags[1:]:
        career_name = tag.find('a').get_text()
        url = tag.find('a')['href']
        career_url = f'{CAREERS_URL}{url}'

        career = Career(name=career_name, page_url=career_url)

        careers.append(career)

    return University(
        name="Universidad de Santander",
        page_url=UDES_BASE_URL,
        careers=careers
    )
