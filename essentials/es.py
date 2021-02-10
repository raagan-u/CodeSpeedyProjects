import http.server , subprocess as sp, socketserver
import os, hashlib
import smtplib, socket, base64
import scapy.all as scapy

def run_server(port, directory):
	os.chdir(os.path.abspath(directory))
	address = ('', int(port))
	handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(address, handler)
	print(f"serving on 0.0.0.0 on port {port}")
	httpd.serve_forever()
	
def send_mail(sender, recepient, message):
	smtp_server = smtplib.SMTP("www.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login(input("Enter Name"), input("Enter Password"))
	smtp_server.sendmail(sender, recepient, message)
	smtp.quit()

def get_ip():
	host_name = socket.gethostname()
	ip = socket.getaddrinfo(host_name, port = 80)
	ipv4, ipv6 = ip[0][4][0], ip[1][4][0]
	print(f"Your IPv4 Addreess is {ipv4}\nYour IPv6 Address is {ipv6}")

def hex():
	encoded = base64.b64encode(bytes(input("String To Be Encoded>> "), 'utf-8'))
	decode = base64.b64decode(encoded)
	print(f"your encoded message is {encoded}\nYour decoded message is {decode}")

def git_functionality():
	# gitpython 
	pass

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

def blue_tooth():
	pass

def ftp():
	pass

def scan_net(ip):
	arp = scapy.ARP(pdst = ip)
	bc = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_bc = bc/arp
	available = scapy.srp(arp_bc, timeout=1)[0]
	print(*available)
	pass

def send_reqs(url):
	resp = requests.get(url)
	resp_1 = requests.post(url, data = None, json= None)

