from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

# Create database
db = SQLAlchemy()


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(length=250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(length=250), nullable=False)
    rating: Mapped[str] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(length=250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(length=250), nullable=False)
