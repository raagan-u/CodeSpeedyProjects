import http.server 

def run_server():
	server_class , handler = http.server.HTTPServer , http.server.BaseHTTPRequestHandler
	httpd = server_class(('', 8000), handler)
	httpd.serve_forever()

def send_mail():
	# smtp or gmail api
	pass

def pipenv_setup():
	pass

def git_functionality():
	# gitpython 
	pass

def sys_log():
	pass

def hex():
	pass

def sha256():
	pass

def md5():
	pass

def blue_tooth():
	pass

def yt_api():
	# https://github.com/youtube/api-samples/tree/master/python
	pass

def ftp():
	pass

print("Welcome To The_Script")
ch = int(input("1.Create A Server for file_transfer\n2.Create A FTP Server\n3.Exit"))
while ch != 3:
	if ch == 1:
		run_server()

# heap memory allocation in python 
# sortings
