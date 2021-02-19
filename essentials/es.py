#!/usr/bin/python3
import http.server, socketserver
import os, hashlib, smtplib, socket, base64, sys
import scapy.all as scapy
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer

__all__ = ["http_server", "get_ip", "b64", "enc_dec", "scan_net", "ftp_server", "rot_alg", "port_scanner"]

def http_server():
	port, directory = int(input("Enter Port ")), input("Enter directory ")
	os.chdir(os.path.abspath(directory))
	address = ('', int(port))
	handler = http.server.SimpleHTTPRequestHandler
	with socketserver.TCPServer(address, handler) as httpd:
		print(f"serving on 0.0.0.0 on port {port}")
		httpd.serve_forever()
	
def get_ip():
	# this won't work for linux users that have /etc/hosts configs 
	host_name = socket.gethostname()
	ip = socket.getaddrinfo(host_name, port = 80)
	ipv4, ipv6 = ip[0][4][0], ip[1][4][0]
	print(f"Your IPv4 Addreess is {ipv4}\nYour IPv6 Address is {ipv6}")

def b64():
	ch = int(input("1.Encode\n2.Decode"))
	if ch == 1:
		# encoding errors
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

def scan_net():
	# windows user must have winpcap inorder to use this module
	# winpacap is the standard windows packet capture library
	# https://www.winpcap.org/install/default.htm
	ip = input("Enter IP or any other valid CIDR Notation")
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

def ftp_server():
	port = int(input("Enter port "))
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
	addr = ('', port)
	with FTPServer(addr, handler) as srvr:
		srvr.serve_forever()

def rot_alg(num): 
	for c in (65, 97):
		for i in range(26):
			d[chr(i+c)] = chr((i+num) % 26 + c)

def port_scanner():
	pass
funcs = {1: http_server, 2: get_ip, 3: b64, 4: enc_dec, 5: scan_net, 6: ftp_server, 7: rot_alg, 8: port_scanner}
if __name__ == "__main__":
	ch = 1
	while ch !=0:
		print("Welcome to Simple Script")
		print("List of available functions\n1.http_server\n2.get_ip\n3.base64\n4.enc_dec\n5.scan_net\n6.ftp_server\n7.rot_alg\n8.port_scanner")
		ch = int(input("Enter Choice (1...10)\n 0 for exit\n >> "))
		funcs[ch]()
	print("Exiting...")
