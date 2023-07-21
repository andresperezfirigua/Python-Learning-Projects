import requests

USERNAME = 'andresperezfirigua'
TOKEN = 'sfvisyb45t34r3jb453bj'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'kuro'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)
