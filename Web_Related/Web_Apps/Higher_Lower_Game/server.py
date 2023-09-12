import random

from flask import Flask

app = Flask(__name__)

answer = random.randint(0, 10)


def center_element(function):
    def wrapper(*args, **kwargs):
        return f'<center>{function(kwargs["number"])}</center>'

    wrapper.__name__ = function.__name__
    return wrapper


@app.route('/')
def home():
    return '<center><h1>Guess a number between 0 and 9</h1></center>' \
           '<center><img src="https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif" width=200></center>'


@app.route('/<number>')
@center_element
def check_guess(number):
    try:
        number = int(number)

    except ValueError:
        return '<h3 style="color: blue">Please enter a number!</h3>' \
               '<img src="https://media.giphy.com/media/lnhOzj6RHueJq5Jgph/giphy.gif" width=200>'

    else:
        if number < answer:
            return '<h1 style="color: red">Too low, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/mhxZiXPbpF8QmtJe7Q/giphy.gif" width=200>'
        elif number > answer:
            return '<h1 style="color: purple">Too high, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/S3toMKZkxGf88V36Ki/giphy.gif" width=200>'
        else:
            return '<h1 style="color: green">You found me!</h1>' \
                   '<img src="https://media.giphy.com/media/4ZpPvSoATPY4Gl7R1A/giphy.gif" width=200>'


if __name__ == '__main__':
    app.run(debug=True)
