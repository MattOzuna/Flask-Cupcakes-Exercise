from flask import Flask, render_template, flash, redirect, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake"
app.config["SQLALCHEMY_BINDS"] = {"testing": "postgresql:///cupcakes_test"}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)

@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
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
                         image= request.json['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize_cupcake()), 201)