import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class OLX_listing:

    def __init__(self, URL, search_object):
        self.URL = urljoin(URL, search_object)
        self.search_object = search_object

        page = requests.get(f"{self.URL}/?search%5Border%5D=created_at:desc")
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('a')
        self.lines = [str(result.get('href')) for result in results]
        self.offer_links = self.get_links()


    def get_page_number(self):
        number_of_pages = 1
        pages = [page for page in self.lines if page.startswith(f"https://www.olx.pl/oferty/{self.search_object}/?page")]
        if pages:
            number_of_pages = pages[-2].lstrip(f'https://www.olx.pl/oferty/q-{self.search_object}/?page=')
        return number_of_pages


    def get_all_pages_offer(self):
        for page_number in range(2, 25):
            self.pageURL = f'https://www.olx.pl/oferty/q-{self.search_object}/?page={page_number}'
            page = requests.get(self.pageURL)
            soup = BeautifulSoup(page.content, "html.parser")
            results = soup.find_all('a')
            lines = [str(result.get('href')) for result in results]
            self.lines.extend(lines)
        self.offer_links = self.get_links()

    def get_links(self):
        offer_links =  [offer for offer in self.lines if str(offer).startswith('https://www.olx.pl/d/oferta/')]
        return offer_links
