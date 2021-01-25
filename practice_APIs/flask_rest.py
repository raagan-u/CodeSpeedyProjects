from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def root_handler():
	return jsonify({ 'name': 'unknown' })

app.run(debug=True, host='0.0.0.0')
