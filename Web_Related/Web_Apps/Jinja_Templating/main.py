import requests
from flask import Flask, render_template
from post import Post

blog_url = 'https://api.npoint.io/e0f0a1d58193f10e815c'
response_posts = requests.get(url=blog_url).json()
posts = [Post(id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body']) for post in response_posts]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<int:p_id>')
def post(p_id):
    requested_post = None
    for post in posts:
        if post.id == p_id:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
