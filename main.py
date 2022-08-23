from time import sleep
from Classes.Classes import OLX_listing

#search object q-name-2ndpartname
search_object = "gra planszowa"
URL = "https://www.olx.pl/api/v1/offers/?offset=0&limit=40&"

'''
Get current offer for products
'''

current_offer = OLX_listing(URL, search_object)

'''
Checking for updates
'''

while True:
    new_offer = OLX_listing(URL, search_object)
    new_offers = [new_link for new_link in set(new_offer.links) if new_link not in current_offer.links]
    print(len(new_offer.links))
    print(new_offer.links)
    if new_offers:
        current_offer.links.extend(new_offers)
    print(f" New listings : {new_offers}")
    sleep(600)



