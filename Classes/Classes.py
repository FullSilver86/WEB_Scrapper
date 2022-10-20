import requests
from time import sleep
import json

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

        converted_to_json = json.loads(page.text)
        for object in enumerate(converted_to_json["data"]):
            # following options cause problems
            # {'highlighted': True, 'urgent': False, 'top_ad': True, 'options': ['bundle_optimum'], 'b2c_ad_page': True, 'premium_ad_page': True}
            if not any(converted_to_json["data"][object[0]]["promotion"].values()):
                self.links.append(converted_to_json["data"][object[0]]["url"])


#to do remove this class

class Session_OLX:


    def __init__(self, search_object):
        self.search_object = search_object
        self.listing = OLX_listing(self.search_object).links







