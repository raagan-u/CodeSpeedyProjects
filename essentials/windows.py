# my simple ftp client for windows nothing special in here
import argparse, ftplib

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-ip', '--host-ip', dest="ip" , help=" specify the ip address to connect")
	parser.add_argument('-p', '--port', dest="port", type=int,  help=" specify the port(default_val is 21)")
	args = parser.parse_args()
	return args

def connect_and_do(addr):
	server = ftplib.FTP()
	server.connect(addr.ip, addr.port)
	server.login('user1', '$password')
	server.dir()

if __name__ == "__main__":
	connect_and_do(get_args())

