#!/usr/bin/python3
import requests as req
import argparse, json, sys

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--method",dest="method",  type=str, help=" specify the http method to use ")
	parser.add_argument("-u", "--url",dest="url",  type=str, help=" specify the url ")
	parser.add_argument("-j", "--json", dest='jsons', type=str, help=" optional json input ", default=None)
	args = parser.parse_args()
	return args

def conv_json(json_str):
	if json_str:
		json_obj = json.loads(json_str)
		return json_obj
	else:
		return None

def do_get(url, jsons=None):
	resp = req.get(url)
	return resp.status_code, resp.text

def do_post(url, jsons=None):
	resp = req.post(url, json=conv_json(jsons))
	return resp.status_code, resp.text


def do_put(url, jsons=None):
	resp = req.put(url, json=conv_json(jsons))
	return resp.status_code, resp.text

def do_patch(url, jsons=None):
	resp = req.patch(url, json=conv_json(jsons))
	return resp.status_code, resp.text

def do_delete(url, jsons=None):
	resp = req.delete(url)
	return resp.status_code, resp.text

funcs = {"do_get":do_get, "do_put":do_put, "do_post":do_post, "do_patch":do_patch, "do_delete":do_delete}
if __name__ == "__main__":
	val = vars(get_args())
	method = val.pop("method")
	values = val.values()
	if method in locals() and callable(locals()[method]):
		print(*(locals()[method](*values)), sep="\n")
