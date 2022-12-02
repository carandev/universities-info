import requests
from models.subject import Subject
import pytesseract
from PIL import Image
from urllib.request import urlopen
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University

UDI_URL = "https://www.udi.edu.co"
CAREER_UDI_URL = f"{UDI_URL}/programas"


def get_UDI_data():
    request = requests.get(CAREER_UDI_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    span_tags = soup.find(
        'ul', {'id': 'div-subcarreras-cat-pregrados'}).find_all('li')
    careers = []

    for tag in span_tags:
        career_name = tag.get_text().strip()
        url = tag.find('a')['href']
        career_url = f'{UDI_URL}{url}'

        subjects = get_subjects(career_url)

        careers.append(Career(
            name=career_name,
            page_url=career_url,
            subjects=subjects
        ))

    return University(
        name="Universidad de Investigación y Desarrollo",
        page_url=UDI_URL,
        careers=careers
    )


def get_subjects(url):
    subject_request = requests.get(url)
    subject_soup = BeautifulSoup(subject_request.content, 'html.parser')
    div_container = subject_soup.find('div', {'id': 'post-malla-curricular'})
    images = div_container.find_all('img')

    subjects = []

    if len(images) <= 0:
        ul_subjects = div_container.find_all('ul')
        for i in range(len(ul_subjects)):
            li_subjects = ul_subjects[i].find_all('li')
            name = ''

            for subject in li_subjects:
                name = subject.get_text().strip().replace('\n', ' ').replace('\t', ' ')

            subjects.append(Subject(
                name=name,
                semester=i+1
            ))
    else:
        for i in range(len(images)):
            image_url = f'{UDI_URL}{images[i]["src"]}'
            text = pytesseract.image_to_string(
                Image.open(urlopen(image_url)), lang="spa")
            image_subjects = text.splitlines()
            name = ''

            for j in range(1, len(image_subjects)):
                if image_subjects[j].strip() != '':
                    name = image_subjects[j].strip()

            subjects.append(Subject(
                name=name,
                semester=i+1
            ))

    return subjects
