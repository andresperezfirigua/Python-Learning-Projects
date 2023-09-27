# import datetime
# import random
# import requests
#
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     current_year = datetime.datetime.now().year
#     print(current_year)
#     random_number = random.randint(0, 10)
#     return render_template('index.html', num=random_number, year=current_year)
#
#
# @app.route('/guess/<name>')
# def guess(name):
#     name = name.title()
#     params = {
#         'name': name
#     }
#     age_response = requests.get(url='https://api.agify.io', params=params)
#     gender_response = requests.get(url='https://api.genderize.io', params=params)
#
#     age = age_response.json()['age']
#     gender = gender_response.json()['gender']
#
#     return render_template('guess.html', age=age, gender=gender, name=name)
#
#
# @app.route('/blog')
# def blog():
#     blog_url = 'https://api.npoint.io/e0f0a1d58193f10e815c'
#     response = requests.get(url=blog_url)
#     return render_template('blog.html', posts=response.json())
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
