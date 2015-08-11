#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import threading
import signal
import info.server_info as server_info
import info.project_info as project_info
from websocket.server_websocket import start_websocket_server

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler): 
 
    def do_GET(self):
    	print self.path
    	if self.path == '/info':
    		data = {}
    		data['services'] = server_info.getServices()
    		data['projects'] = project_info.getProjects()

    		self.wfile.write(str(data))
    	else:
        	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self) 
 
    def do_POST(self): 
        form = cgi.FieldStorage() 
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_POST(self) 


def start_http_server():
	PORT = 8000
	handler = ServerHandler
	httpd = SocketServer.TCPServer(("", PORT), handler)
	print "Serving HTTP at port", PORT
	while keep_running():
		httpd.handle_request()

KEEP_RUNNING = True

def signal_handler(signal, frame):
	print 'Ctrl+C pressed. Stopping HTTP Server'
	global KEEP_RUNNING
	KEEP_RUNNING = False

def keep_running():
    return KEEP_RUNNING

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	threading.Thread(target=start_http_server).start()
	start_websocket_server()
