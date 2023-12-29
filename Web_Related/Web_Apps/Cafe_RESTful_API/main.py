from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route('/random')
def get_random_cafe():
    # cafes = db.session.execute(db.select(Cafe.id)).scalars().all()
    # random_cafe = rdm.choice(cafes)
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    # cafe = db.get_or_404(Cafe, random_cafe)
    return jsonify(cafe=random_cafe.to_dict())

    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price
    # })


@app.route('/all')
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])


@app.route('/search')
def search_cafe():
    cafe_location = request.args.get('loc')
    found_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location.title()).order_by(Cafe.name)).scalars().all()

    if not found_cafes:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        }), 404

    return jsonify(cafe=[cafe.to_dict() for cafe in found_cafes])

# HTTP POST - Create Record


@app.route('/add', methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={
        "success": "The cafe has been successfully added"
    })

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
