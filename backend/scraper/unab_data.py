import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University

UNAB_URL = "https://unab.edu.co"
CAREERS_UNAB_URL = f"{UNAB_URL}/pregrados/"


def get_UNAB_data():
    request = requests.get(CAREERS_UNAB_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    h2_tags = soup.find_all('h2')

    careers = []

    for tag in h2_tags[:-13]:
        career_name = tag.get_text().strip()
        career_url = tag.find('a')['href']

        career = Career(name=career_name, page_url=career_url)
        careers.append(career)

    return University(
        name="Universidad Autónoma de Bucaramanga",
        page_url=UNAB_URL,
        careers=careers
    )
