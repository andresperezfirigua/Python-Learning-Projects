from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from data_manager import db, Movie
from rate_movie_form import RateMovieForm
from add_movie_form import AddMovieForm
import requests
import os

tmdb_key = os.environ.get('TMDB_Key')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db.init_app(app)


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
    all_movies = result.all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template('index.html', movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        params = {
            'query': add_form.title.data,
            'api_key': tmdb_key
        }
        response = requests.get(url='https://api.themoviedb.org/3/search/movie', params=params)
        return render_template('select.html', movies=response.json()['results'])

    return render_template('add.html', form=add_form)


@app.route('/search')
def search():
    movie_id = request.args.get('id')
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'api_key': tmdb_key
    }

    selected_movie = requests.get(url=url, params=params).json()

    new_movie = Movie(
        title=selected_movie['title'],
        year=int(selected_movie['release_date'].split('-')[0]),
        description=selected_movie['overview'],
        img_url=f"https://image.tmdb.org/t/p/original/{selected_movie['poster_path']}"
    )

    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit_form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = db.get_or_404(Movie, movie_id)
    title = movie_to_update.title

    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=edit_form, title=title)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
