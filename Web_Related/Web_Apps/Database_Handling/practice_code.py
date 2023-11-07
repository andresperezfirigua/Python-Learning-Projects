# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

# Create database
db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_books_collection.db"

db.init_app(app)


# Create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(length=250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(length=250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# Insert object/record to database

with app.app_context():
    book = Book(
        title="Emi",
        author="Edgar Poe",
        rating=9.0
    )

    db.session.add(book)
    db.session.commit()

# Get all data in table

with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    for book in all_books:
        print(book.title)

# Get a single row of data from table

with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == 'Mobydick')).scalar()
    print(f'{book.rating}\n{book.author}')

# Update single row in table by title name using a query

with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == 'Silvia')).scalar()
    book_to_update.title = 'Edwin'
    db.session.commit()

# Update single row in table by Primary Key

with app.app_context():
    book_id = 4
    book_update = db.get_or_404(Book, book_id)
    book_update.title = 'Jaime'
    db.session.commit()

# Delete a row in table by Primary Key and also by query

with app.app_context():
    book_id = 6
    book_title = 'Maic'

    first_book_to_delete = db.session.execute(db.select(Book).where(Book.title == book_title)).scalar()
    db.session.delete(first_book_to_delete)

    second_book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(second_book_to_delete)

    db.session.commit()


# db = sqlite3.connect('testDB.db')
#
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE books "
#                "("
#                "id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL"
#                ")"
#                )
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K Rowling', '9.3')")
# db.commit()
