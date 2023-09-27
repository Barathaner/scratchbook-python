import requests
from bs4 import BeautifulSoup

URL = 'https://laracon.net/'  # Ersetzen Sie dies durch die tatsächliche URL, auf der die Talks gelistet sind
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Dies hängt vom tatsächlichen Layout der Website ab
talks = soup.find_all('div', class_='talk')  # Ersetzen Sie 'div' und 'talk' durch die tatsächlichen HTML-Tag und Klasse

for talk in talks:
    title = talk.find('h2').text
    speaker = talk.find('p', class_='speaker').text
    print(f'Title: {title}, Speaker: {speaker}')
