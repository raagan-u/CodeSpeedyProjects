#!/usr/bin/python3
import requests as req
import sys
import argparse, json

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--method",dest="method",  type=str, help=" specify the http method to use ")
	parser.add_argument("-u", "--url",dest="url",  type=str, help=" specify the url ")
	parser.add_argument("-j", "--json", dest='jsons', type=str, help=" optional json input ", default=None)
	args = parser.parse_args()
	print(args)
	return args

def do_post(url, jsons=None):
	resp = req.post(url, json=jsons)
	return resp.status_code, resp.text

def do_get(url, jsons=None):
	resp = req.get(url)
	return resp.status_code, resp.text

def put(url, jsons=None):
	resp = req.post(url, json=jsons)
	return resp.status_code, resp.text

def patch(url, jsons=None):
	head = {"content-type": "application/json"}
	resp = req.patch(url, data=jsons, headers=head)
	return resp.status_code, resp.text

def delete(url, jsons=None):
	resp = req.delete(url)
	return resp.status_code, resp.text

if __name__ == "__main__":
	val = vars(get_args())
	method = val.pop("method")
	values = val.values()
	#json_data = json.loads(.jsons)
	if method in locals() and callable(locals()[method]):
		print(*(locals()[method](*values)), sep="\n")

# threading and multiprocessing
 
