import requests

class OLX_listing:



    def __init__(self, URL, search_object):
        self.URL = URL
        self.search_object = search_object
        self.links = []
        user_agent = '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'''
        headers = {'User-Agent': user_agent,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
        page = requests.get(f'''{self.URL}query={self.search_object.replace(' ' , '%20')}&sort_by=created_at%3Adesc&filter_refiners=spell_checker&facets=%5B%7B%22field%22%3A%22region%22%2C%22fetchLabel%22%3Atrue%2C%22fetchUrl%22%3Atrue%2C%22limit%22%3A30%7D%2C%7B%22field%22%3A%22category_without_exclusions%22%2C%22fetchLabel%22%3Atrue%2C%22fetchUrl%22%3Atrue%2C%22limit%22%3A20%7D%5D&sl=180b26a0c03x6be1b302''', headers=headers)

        api_response = list(page.text.split())
        x = [url for url in api_response if 'https://www.olx.pl/d/oferta/' in url]
        for y in x:
            link = self.substring_after(y, "url").split('''"''')[2]
            self.links.extend([link])



    def substring_after(self, x, delim):
            return x.partition(delim)[2]

