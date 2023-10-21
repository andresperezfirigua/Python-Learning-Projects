from flask import Flask, render_template, request
from login_form import LoginForm
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = 'Type any secret key here'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_info = {
        'email': 'admin@email.com',
        'password': 'test'
    }
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == login_info['email'] and form.password.data == login_info['password']:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
