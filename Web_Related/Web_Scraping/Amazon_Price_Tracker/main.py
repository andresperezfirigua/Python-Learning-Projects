from datamanager import DataManager
from emailhandler import EmailHandler

lowest_price = 28.49

datamanager = DataManager()

datamanager.scrape_price()

if abs(datamanager.price - lowest_price) < 1.5:
    emailhandler = EmailHandler(datamanager.url, datamanager.product, datamanager.price)
    emailhandler.send_price_alert()
