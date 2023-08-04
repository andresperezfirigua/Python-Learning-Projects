import requests

questions_url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'

parameters = {
    'amount': 10,
    'category': 18,
    'type': 'boolean'
}

data = requests.get(url=questions_url, params=parameters, verify=False)
data.raise_for_status()
question_data = data.json()['results']
