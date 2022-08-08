import requests
from bs4 import BeautifulSoup


class OLX_listing:


    def get_new_offer(self, URL, previous_offer):
        self.URL = URL
        self.previous_offers = previous_offer

        new_offer = []
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all('a')
        lines = [str(result.get('href')) for result in results]
        for link in lines:
            if link.startswith('/d/oferta/'):
                if link not in previous_offer:
                    print(f"Nowa oferta:{link} ")
                    new_offers.append(link)
        return new_offer
