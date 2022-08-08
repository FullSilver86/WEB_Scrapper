import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
from Classes.Classes import OLX_listing

#search object q-"name"
search_object = "q-wing-foil"
URL = urljoin("https://www.olx.pl/oferty/", search_object)
print(URL)

'''
Get current offer for products
'''
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all('a')
lines = [str(result.get('href')) for result in results]
links = [link for link in lines if link.startswith('https://www.olx.pl/d/oferta/')]


while True:
    new_links = OLX_listing()
    new_links.get_new_offer(URL, links)
    sleep(600)