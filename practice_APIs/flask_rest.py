import os
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# setting up the db path 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#setting up serializer for easy working
se = Marshmallow(app)


db = SQLAlchemy(app)

#creating fields 
class Sample(db.Model):
	ide = db.Column(db.Integer, primary_key=True)
	field1 = db.Column(db.String(35))
	field2  = db.Column(db.String(35))

	#def __init__(self, ide, field1, field2):
	def __init__(self, req_json):
		#self.ide = ide
		#self.field1 = field1
		#self.field2 = field2
		self.ide = req_json['ide']
		self.field1 = req_json['field1']
		self.field2 = req_json['field2']

#setting up how the data should be serialized and ouput to be given
class Sample_Schema(se.Schema):
	class Meta:
		fields = ('ide', 'field1', 'field2')		

sample_schema = Sample_Schema()
#sample_schemas = Sample_Schema(many=True)

#setting up route
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
	#ide = request.json['ide']
	#field1 = request.json['field1']
	#field2 = request.json['field2']
	#temp_obj = Sample(ide, field1, field2)
	temp_obj = Sample(request.json)
	db.session.add(temp_obj)
	db.session.commit()

	return sample_schema.jsonify(temp_obj)

@app.route("/putting/<collection>", methods = ['PUT'])
def putting(collection):
	temp_obj = Sample.query.get(collection)
	if temp_obj:
		return sample_schema.jsonify(temp_obj), 201
	else:
		temp_obj = Sample(request.json)
		db.session.add(temp_obj)
		db.session.commit()
		return sample_schema.jsonify(temp_obj), 200

@app.route("/patching/<collection>", methods = ['PATCH'])
def patching(collection):
	temp_obj = Sample.query.get(collection)
	if temp_obj:
		temp_obj.field1, temp_obj.field2 = request.json['field1'], request.json['field2']
		db.session.add(temp_obj)
		db.session.commit()
		return jsonify({'process': 'updated'}), 201

	temp_obj = Sample(request.json)
	db.session.add()
	db.session.commit()
	return jsonify({'process': 'created'}), 200

@app.route("/deleteing/<collection>", methods = ['DELETE'])
def deleting(collection):
	temp_obj = Sample.query.get(collection)
	if temp_obj:
		db.session.delete(temp_obj)
		db.session.commit()
		return jsonify({"deleted": "yes"}), 200

	return jsonify({"record": "not found"}), 404

logging.basicConfig(filename='flask_session.log',
						level=logging.DEBUG,
							format=’%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s’)
# also need to add logger
app.run(debug=True)