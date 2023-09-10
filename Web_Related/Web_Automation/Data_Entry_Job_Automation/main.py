from datamanager import DataManager
from formhandler import FormHandler

datamanager = DataManager()

properties = datamanager.search_data()

form_handler = FormHandler()

for item in properties:
    form_handler.fill_in_form(item)

form_handler.driver.quit()
