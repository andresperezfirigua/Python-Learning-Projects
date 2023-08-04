import datetime

import requests

# Creating an account in Pixela using an HTTP Post request

USERNAME = 'Create a username here'
TOKEN = 'Create a token here'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph in my Pixela account using an HTTP Post request

graph_id = 'graph1'

graph_config = {
    'id': graph_id,
    'name': 'Coding Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'kuro'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

# Creating a pixel in my Pixela graph using an HTTP Post request

# date = datetime.datetime(year=2023, month=7, day=22).strftime("%Y%m%d")
date = datetime.datetime.now().strftime("%Y%m%d")

pixel_config = {
    'date': date,
    'quantity': '10'
}

create_pixel_endpoint = f'{graph_endpoint}/{graph_id}'

# response = requests.post(url=create_pixel_endpoint, json=pixel_config, headers=headers)

# print(response.status_code)

# Updating a pixel in my Pixela graph using an HTTP Put request

# update_pixel_endpoint = f'{create_pixel_endpoint}/{date}'

update_pixel_config = {
    'quantity': '8'
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.status_code)

# Deleting a pixel from my Pixela graph using an HTTP Delete request

delete_pixel_endpoint = f'{create_pixel_endpoint}/{date}'

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.status_code)
