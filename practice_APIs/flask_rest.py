import os
from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_rest.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


se = Marshmallow(app)
db = SQLAlchemy(app)



@app.route("/", methods = ['GET'])
def root_handler():
	return jsonify({ 'name': 'unknown' })

@app.route("/new", methods = ['GET'])
def new_dir():
	return jsonify({ 'test': 'testing'})
app.run(debug=True, host='0.0.0.0')
