from time import sleep
# from telesign.messaging import MessagingClient
from Classes.Classes import OLX_listing

#search object q-"name-2ndpartname"
search_object = "q-gry-planszowe"
URL = "https://www.olx.pl/oferty/"

'''
Get current offer for products
'''

current_offer = OLX_listing(URL, search_object)
current_offer.get_all_pages_offer()
print(current_offer.URL)
'''
Checking for updates
'''

while True:
    new_offer = OLX_listing(URL, search_object)
    new_offers = [new_link for new_link in set(new_offer.offer_links) if new_link not in current_offer.offer_links and "promoted" not in new_link]
    print(len(new_offer.offer_links))
    print(new_offer.offer_links)
    if new_offers:
        current_offer.offer_links.extend(new_offers)
    print(f" New listings : {new_offers}")
    sleep(600)



