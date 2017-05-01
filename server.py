#!/usr/bin/env python

import sys
import time
import BaseHTTPServer
from random import randint

HOST_NAME = '127.0.0.1'
PORT_NUMBER = 5051 #int(sys.argv[1])

class HiHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        time.sleep(randint(0,10))
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("Hi!\n")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HiHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
