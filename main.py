import requests
from bs4 import BeautifulSoup
from time import sleep

URL = "https://www.olx.pl/d/sport-hobby/q-wing-foil/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all('a')

lines = [str(result.get('href')) for result in results]
links = [ link for link in lines if link.startswith('/d/oferta/')]

# lal
while True:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all('a')
    lines = [str(result.get('href')) for result in results]
    for link in lines:
        if link.startswith('/d/oferta/'):
            if link not in links:
                print(f"Nowa oferta:{link} ")
    sleep(600)