from time import sleep

from Classes.Classes import OLX_listing

#search object q-"name-2ndpartname"
search_object = "q-gry-planszowe"
URL = "https://www.olx.pl/oferty/"

'''
Get current offer for products
'''

current_offer = OLX_listing(URL, search_object)

'''
Checking for updates
'''

while True:
    new_offer = OLX_listing(URL, search_object)
    new_offers = [new_link for new_link in new_offer.offer_links if new_link not in current_offer.offer_links]
    print(current_offer.offer_links)
    print(new_offer.offer_links)
    print(f" New listings : {new_offers}")
    sleep(600)
