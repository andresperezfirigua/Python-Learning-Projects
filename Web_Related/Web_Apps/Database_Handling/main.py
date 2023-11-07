from flask import Flask, render_template, request, redirect, url_for
from data_manager import Book, db

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books_collection.db"

db.init_app(app)


@app.route('/')
def home():
    all_books = list(db.session.execute(db.select(Book).order_by(Book.title)).scalars())
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(
                title=request.form['title'],
                author=request.form['author'],
                rating=request.form['rating']
            )

            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form["id"]
        book_to_edit = db.get_or_404(Book, book_id)
        book_to_edit.rating = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)

    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

