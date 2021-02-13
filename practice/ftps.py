#!/usr/bin/bash
import logging
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

autho = DummyAuthorizer()
autho.add_user('root', 'toor', '/home', perm='elr')
autho.add_anonymous('.')

handler = FTPHandler
handler.authorizer = autho

logging.basicConfig(filename="./ftpsrvr.log", level=logging.INFO)

addr = ('', 1337)
with FTPServer(addr, handler) as srvr:
	srvr.serve_forever()
