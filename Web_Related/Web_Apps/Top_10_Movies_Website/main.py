from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from data_manager import db, Movie
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db.init_app(app)


@app.route("/")
def home():
    all_movies = list(db.session.execute(db.select(Movie).order_by(Movie.ranking)).scalars())
    return render_template('index.html', movies=all_movies)


@app.route('/edit', methods=['GET', 'POST'])
def edit():

    return render_template('edit.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

# with app.app_context():
        # new_movie = Movie(
        #     title="Avatar The Way of Water",
        #     year=2022,
        #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        #     rating=7.3,
        #     ranking=9,
        #     review="I liked the water.",
        #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        # )
        #
        # db.session.add(new_movie)
        # db.session.commit()
