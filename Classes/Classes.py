import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class OLX_listing:
    URL = ""
    # lines are required for getting number of pages and correct offer links [used by multiple methods]
    lines = []
    search_object = ''
    number_of_pages = 1
    offer_links = []


    def __init__(self, URL, search_object):
        self.URL = urljoin(URL, search_object)
        self.search_object = search_object

        OLX_listing.URL = self.URL
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('a')
        lines = [str(result.get('href')) for result in results]
        OLX_listing.lines = lines
        OLX_listing.search_object = search_object
        OLX_listing.number_of_pages = int(self.get_page_number())
        if OLX_listing.number_of_pages > 1:
            for page_number in range(2, int(OLX_listing.number_of_pages)+1):
                OLX_listing.lines.extend(self.get_all_pages_offer(f'https://www.olx.pl/oferty/q-{search_object}/?page={page_number}'))
        self.get_links()
        print(self.URL)


    def get_page_number(self):
        number_of_pages = 1
        pages = [page for page in OLX_listing.lines if page.startswith(f"https://www.olx.pl/oferty/{OLX_listing.search_object}/?page")]
        if pages:
            number_of_pages = pages[-2].lstrip(f'https://www.olx.pl/oferty/q-{OLX_listing.search_object}/?page=')
        return number_of_pages


    def get_all_pages_offer(self, pageURL):
        self.pageURL = pageURL
        page = requests.get(self.pageURL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('a')
        lines = [str(result.get('href')) for result in results]
        return lines


    def get_links(self):
        OLX_listing.offer_links =  [offer for offer in OLX_listing.lines if str(offer).startswith('https://www.olx.pl/d/oferta/')]
