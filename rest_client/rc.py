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
	args = get_args()
	json_data = json.loads(args.jsons)
	print(json_data, type(json_data))
	if args.method in locals() and callable(locals()[args.method]):
		print(*(locals()[args.method](args.url, json_data)), sep="\n")
# fix json erros?!!!!
