# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_books_collection.db"

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(length=250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(length=250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    book = Book(
        title="Harry Potter",
        author="J. K. Rowling",
        rating=9.3
    )

    db.session.add(book)
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
