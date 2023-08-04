import requests
import os
import datetime as dt

#|--------------------------------- Request for Nutritionix exercise API  -------------------------------------------|#

# Credentials for nutritionix
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2'

exercise_endpoint = f'{nutritionix_endpoint}/natural/exercise'

user_input = input('Tell which exercises you did today: ')

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

nutritionix_params = {
    'query': user_input
    # 'gender':
    # 'weight_kg':
    # 'height_cm':
    # 'age':
}

exercise_response = requests.post(url=exercise_endpoint, json=nutritionix_params, headers=nutritionix_headers)

print(exercise_response.json())

#|--------------------------- Request for Sheety Google spreadsheet API -------------------------------------|#

nutritionix_response = exercise_response.json()

# Credentials for sheety
authorization_key = os.environ.get('authorization_key')

sheety_endpoint = os.environ.get('sheety_endpoint')

sheety_headers = {
    'Authorization': authorization_key,
    'Content-Type': 'application/json'
}


for exercise in nutritionix_response['exercises']:
    new_row_params = {
        'workout': {
            'date': dt.datetime.now().strftime('%x'),
            'time': dt.datetime.now().strftime('%X'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=new_row_params, headers=sheety_headers)
    print(sheet_response.status_code)
    print(sheet_response.json())
