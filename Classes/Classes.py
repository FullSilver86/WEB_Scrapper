import requests
from time import sleep

class OLX_listing:


    def __init__(self, search_object, URL = 'https://www.olx.pl/api/v1/offers/?offset=0&limit=40&'):
        self.URL = URL
        self.search_object = search_object
        self.links = []
        user_agent = '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko)'''
        '''Version/10.0.1 Safari/602.2.14'''
        headers = {'User-Agent': user_agent,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        page = requests.get(f'''{self.URL}query={self.search_object.replace(' ' , '%20')}&sort_by=created_at%3Adesc'''
        '''&filter_refiners=spell_checker&facets=%5B%7B%22field%22%3A%22region%22%2C%22fetchLabel%22%3Atrue%2C%22fetch'''
        '''Url%22%3Atrue%2C%22limit%22%3A30%7D%2C%7B%22field%22%3A%22category_without_exclusions%22%2C%22fetchLabel'''
        '''%22%3Atrue%2C%22fetchUrl%22%3Atrue%2C%22limit%22%3A20%7D%5D&sl=180b26a0c03x6be1b302''', headers=headers)

        api_response = list(page.text.split())
        listing = [url for url in api_response if 'https://www.olx.pl/d/oferta/' in url]
        for line in listing:
            link = self.substring_after(line, "url").split('''"''')[2]
            self.links.extend([link])



    def substring_after(self, line, delim):
            return line.partition(delim)[2]


class Session_OLX:


    def __init__(self, search_object):
        self.search_object = search_object
        self.listing = self.main()


    def main(self):
        '''
          Get current offer for products
          '''
        current_offer = OLX_listing(self.search_object)

        '''
        Checking for updates
        '''

        # while True:
        new_offer = OLX_listing(self.search_object)
        new_offers = [new_link for new_link in set(new_offer.links) if new_link not in current_offer.links]
        print(len(new_offer.links))
        print(new_offer.links)
        if new_offers:
            current_offer.links.extend(new_offers)
        print(f" New listings : {new_offers}")
        return new_offer.links
            # sleep(500)