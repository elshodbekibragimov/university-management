from flask import render_template, redirect, url_for
from app import app, db

@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html")