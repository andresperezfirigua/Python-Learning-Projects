import requests
import email_service
from flask import Flask, render_template, request

app = Flask(__name__)

blog_url = 'https://api.npoint.io/930f7e16959b596f27ec'
posts = requests.get(blog_url).json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email_service.send_email(request.form)
        return render_template('contact.html', sent=True)
    return render_template('contact.html', sent=False)


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for p in posts:
        if p['id'] == post_id:
            requested_post = p
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
