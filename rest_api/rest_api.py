import os
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)

# database setup
basedir = os.path.abspath(os.path.dirname(__file__))
# also can use other sql dbs instead of sqlite .
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# serializer and db init
se = Marshmallow(app)
db = SQLAlchemy(app)

# fields for db
class Sample(db.Model):
	ide = db.Column(db.Integer, primary_key=True)
	field1 = db.Column(db.String(35))
	field2  = db.Column(db.String(35))

	def __init__(self, req_json):
		self.ide = req_json['ide']
		self.field1 = req_json['field1']
		self.field2 = req_json['field2']

# setting up serializing
class Sample_Schema(se.Schema):
	class Meta:
		fields = ('ide', 'field1', 'field2')		

sample_schema = Sample_Schema()
sample_schemas = Sample_Schema(many=True)

db.create_all()
# routes with five basic HTTP Methods
@app.route("/", methods = ['GET'])
def root_handler():
	temp_obj = Sample.query.all()
	return sample_schemas.jsonify(temp_obj)

@app.route("/get_data/<int:ide>", methods=['GET'])
def get_data(ide):
	temp_obj = Sample.query.get(ide)
	return sample_schema.jsonify(temp_obj)
	

@app.route("/add", methods = ['POST'])
def add_data():
	db.create_all()
	temp_obj = Sample(request.json)
	db.session.add(temp_obj)
	db.session.commit()
	return sample_schema.jsonify(temp_obj)

@app.route("/putting/<int:ide>", methods = ['PUT'])
def putting(ide):
	temp_obj = Sample.query.get(ide)
	if temp_obj:
		return sample_schema.jsonify(temp_obj), 201
	else:
		temp_obj = Sample(request.json)
		db.session.add(temp_obj)
		db.session.commit()
		return sample_schema.jsonify(temp_obj), 200

@app.route("/patch_data/<int:ide>", methods = ['PATCH'])
def patching(ide):
	temp_obj = Sample.query.get(ide)
	if temp_obj:
		temp_obj.field1, temp_obj.field2 = request.json['field1'], request.json['field2']
		db.session.add(temp_obj)
		db.session.commit()
		return jsonify({'process': 'updated'}), 201

	temp_obj = Sample(request.json)
	db.session.add(temp_obj)
	db.session.commit()
	return jsonify({'process': 'created'}), 200

@app.route("/delete_data/<int:ide>", methods = ['DELETE'])
def deleting(ide):
	temp_obj = Sample.query.get(ide)
	if temp_obj:
		db.session.delete(temp_obj)
		db.session.commit()
		return jsonify({"deleted": "yes"}), 200

	return jsonify({"record": "not found"}), 404

# optional logging to file
'''logging.basicConfig(filename='flask_session.log',
						level=logging.DEBUG,
							format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
'''
app.run(debug=True)
