import requests as req

def post(url):
	resp = post(url, data=datas, json=samp)
	return resp.status_code, resp.text

def get(url):
	resp = get(url)
	return resp.status_code, resp.text

def put():
	pass

def patch():
	pass

def delete():
	pass

