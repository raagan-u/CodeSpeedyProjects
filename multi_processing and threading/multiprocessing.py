import socket, sys, concurrent.futures as cf

ip = "192.168.1.10"
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scan(port):
	print(f"scanning port {port} ")
	try:
		res = srvr.connect_ex((ip, port))
		if res == 0:
			return f"Port {port} is open "

	except socket.gaierror:
		pass

if __name__ == '__main__':
	#with cf.ThreadPoolExecutor() as executor:
	with cf.ProcessPoolExecutor() as executor:
		results = [executor.submit(scan, i) for i in range(0,100)]

	for f in cf.as_completed(results):
		if f.result():
			print(f.result())
