import os
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

se = Marshmallow(app)
db = SQLAlchemy(app)

class Sample(db.Model):
	ide = db.Column(db.Integer, primary_key=True)
	field1 = db.Column(db.String(35))
	field2  = db.Column(db.String(35))

	def __init__(self, ide, field1, field2):
		self.ide = ide
		self.field1 = field1
		self.field2 = field2

class Sample_Schema(se.Schema):
	class Meta:
		fields = ('ide', 'field1', 'field2')		

sample_schema = Sample_Schema()

@app.route("/", methods = ['GET'])
def root_handler():
	return jsonify({ 'name': 'unknown' })

@app.route("/get_data/<int:ide>", methods=['GET'])
def get_data(ide):
	temp_obj = Sample.query.get(ide)
	return sample_schema.jsonify(temp_obj)
	

@app.route("/add", methods = ['POST'])
def add_data():
	db.create_all()
	ide = request.json['ide']
	field1 = request.json['field1']
	field2 = request.json['field2']
	temp_obj = Sample(ide, field1, field2)
	db.session.add(temp_obj)
	db.session.commit()

	return sample_schema.jsonify(temp_obj)

app.run(debug=True)
