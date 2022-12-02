import requests
from bs4 import BeautifulSoup
from models.career import Career

from models.university import University


UIS_URL = "https://uis.edu.co"
CAREERS_UIS_URL = f"{UIS_URL}/uis-programas-pregrado-es/"


def get_UIS_data():
    get_subjects('https://uis.edu.co/fc-pre-biologia-es/')
    request = requests.get(CAREERS_UIS_URL)

    soup = BeautifulSoup(request.content, 'html.parser')
    h4_tags = soup.find_all('h4')

    careers = []

    for tag in h4_tags:
        career_name = tag.get_text()
        career_url = tag.find('a')['href']

        # get_subjects(career_url)

        career = Career(name=career_name, page_url=career_url)
        careers.append(career)

    return University(
        name="Universidad Industrial de Santander",
        page_url=UIS_URL,
        careers=careers
    )


def get_subjects(url):
    def id_contain(tag):
        if tag.has_attr('id'):
            return 'tab' in tag['id']
        else:
            return False

    subjects_request = requests.get(url)
    subjects_soup = BeautifulSoup(subjects_request.content, 'html.parser')
    subjects_container = subjects_soup.find(
        'div', {'class': 'eael-advance-tabs eael-tabs-horizontal eael-tab-auto-active active-caret-on'})
    semester_container = subjects_container.find_all(id_contain)
    subject_name = ''
    semester = 0

    for i in range(1, len(semester_container) - 1):
        subjects = semester_container[i].find_all('p')
        print(f'--- semester {i} ---')
        for subject in subjects:
            print(subject.get_text().split('-')[-1].replace('\xa0', ''))

    subjects = semester_container[-1].find_all('p')

    print(f'--- semester {semester} ---')
    for subject in subjects:
        print(subject.get_text().split('-')[-1].replace('\xa0', ''))
