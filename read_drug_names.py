from string import ascii_lowercase
from requests import get
from bs4 import BeautifulSoup

url_base = 'https://druginfo.nlm.nih.gov/drugportal/drug/names/'

with open('./names.txt', 'w') as names:
    for letter in ascii_lowercase:
        res = get(url_base + letter)

        soup = BeautifulSoup(res.text)
        table = soup.find(
            'table', {'role': 'presentation'}
        ).find('table', {'border': '1'})
        anchors = table.find_all('a')
        for a in anchors:
            names.write('{}\n'.format(a.string))
