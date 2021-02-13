#!/usr/bin/python3
import http.server, socketserver
import os, hashlib, smtplib, socket, base64
import scapy.all as scapy
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer

def run_server(port, directory):
	os.chdir(os.path.abspath(directory))
	address = ('', int(port))
	handler = http.server.SimpleHTTPRequestHandler
	with socketserver.TCPServer(address, handler) as httpd:
		print(f"serving on 0.0.0.0 on port {port}")
		httpd.serve_forever()
	
def send_mail(sender, recepient, message, body):
	smtp_server = smtplib.SMTP("www.gmail.com",587)
	smtp_server.ehlo()
	smtp_server.starttls()
	smtp_server.login(input("Enter Name"), input("Enter Password"))
	msg = f"\r\nFrom:{sender}\nTo:{recepient}\nSubject:{sub}\n{body})"
	smtp_server.sendmail(sender, recepient, message)
	smtp.quit()

def get_ip():
	host_name = socket.gethostname()
	ip = socket.getaddrinfo(host_name, port = 80)
	ipv4, ipv6 = ip[0][4][0], ip[1][4][0]
	print(f"Your IPv4 Addreess is {ipv4}\nYour IPv6 Address is {ipv6}")

def b64():
	ch = int(input("1.Encode\n2.Decode"))
	if ch == 1:
		encoded = base64.b64encode(bytes(input("String To Be Encoded>> "), 'utf-8'))
		print(f"your encoded message is {encoded}")

	if ch == 2:
		decoded = base64.b64decode(bytes(input("Enter base64 to decode>> "), 'utf-8'))
		print(f"your decoded message is {decoded}")

def enc_dec():
	print("list_of_available_algorithms\n")
	algs = enumerate(list(hashlib.algorithms_guaranteed))
	alg_map = dict()
	for i, j in algs:
		print(f"{i+1}. {j}")
		alg_map[i+1] = j
	else:
		print(f"Enter Your Choice 1 ... {i+1}")
	hash_obj = hashlib.new(alg_map[int(input("choice >>"))])
	hash_obj.update(input("Enter Data to Be Encoded >> ").encode('utf-8'))
	print(hash_obj.hexdigest())

def scan_net(ip):
	arp = scapy.ARP(pdst = ip)
	bc = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_bc = bc/arp
	available = scapy.srp(arp_bc, timeout=1)[0]
	results_list = []
	for element in available:
		result = {'ip':element[1].psrc, 'mac':element[1].hwsrc}
		results_list.append(result)
	
	for i in results_list:
		print(i)

def ftp():
	# should add code for windows
	autho = DummyAuthorizer()
	autho.add_anonymous(os.getcwd())
	autho.add_user('user1', '$password', './', perm='elrarmw')
	handler = FTPHandler
	handler.authorizer = autho
	'''
		e - cd ; l - list_files, r - retreive(read perms)
		the following is write_perms:
		a- append, d - delete , r - rename, m - create dir , 
			w - store file to srvr , M - chmod, T - update file last
										modified time
	'''
	addr = ('192.168.1.10', 1337)
	with FTPServer(addr, handler) as srvr:
		srvr.serve_forever()

def git():
	pass

if __name__ == "__main__":
	ftp()
#https://docs.python.org/3/library/threading.html
