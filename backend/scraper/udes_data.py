import requests
from bs4 import BeautifulSoup
from models.career import Career
from models.subject import Subject

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
        career_url = f'{UDES_BASE_URL}{url}'

        data = get_career_subjects(career_url)

        career = Career(name=career_name, page_url=career_url,
                        price=data['price'], subjects=data['subjects'])

        careers.append(career)

    return University(
        name="Universidad de Santander",
        page_url=UDES_BASE_URL,
        careers=careers
    )


def get_career_subjects(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')

    table = soup.find(
        'table', {'class': 'my-info-valor uk-table uk-table-small'})
    price = table.find_all('td')[5].get_text().strip().replace(
        "'", '').replace("$", '').replace(".", '')

    studies = soup.find('div', {'class': 'moduletable'}).find_all('ul')
    subjects = []

    for i in range(len(studies)):
        for subject in studies[i]:
            a_tag = subject.find('a')
            name = subject.get_text().strip()
            url = ''
            semester = i + 1
            if type(a_tag) is not int:
                if a_tag is not None:
                    url = a_tag['href']

                subjects.append(Subject(
                    name=name,
                    file_url=url,
                    semester=semester
                ))

    return {'subjects': subjects, 'price': price}
