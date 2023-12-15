from flask import Flask, render_template, flash, redirect, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcake"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)