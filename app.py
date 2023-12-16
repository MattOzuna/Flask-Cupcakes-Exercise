from flask import Flask, render_template, flash, redirect, jsonify, request
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake"
app.config["SQLALCHEMY_BINDS"] = {"testing": "postgresql:///cupcakes_test"}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)

##==============================//Front-End Route//==============================##

@app.route('/')
def home_page():
    cupcakes = db.session.query(Cupcake).all()
    form = AddCupcakeForm()
    return render_template('home-page.html', cupcakes=cupcakes, form=form)

##==============================//API Routes//==============================##

@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = db.session.query(Cupcake).all()
    data = [cupcake.serialize_cupcake() for cupcake in cupcakes]
    return jsonify(cupcakes=data)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize_cupcake())


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    new_cupcake= Cupcake(flavor=request.json["flavor"],
                         size=request.json["size"],
                         rating=request.json['rating'],
                         image= request.json['image'] if request.json['image'] else None)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize_cupcake()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize_cupcake())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Cupcake has been deleted')

