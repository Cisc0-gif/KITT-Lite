# -*- coding: utf-8 -*-

import sys
import base64
import BaseHTTPServer

from SimpleHTTPServer import SimpleHTTPRequestHandler


class AuthenticationHandler(SimpleHTTPRequestHandler):
    key = '1234'

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Secure HTTP Environment\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.headers.getheader('Authorization') is None:
            self.do_AUTHHEAD()
            self.wfile.write('No auth received')
        elif self.headers.getheader('Authorization') == 'Basic ' + self.key:
            SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(self.headers.getheader('Authorization'))
            self.wfile.write('Not authenticated')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: SecureHTTPServer.py [port] [username:password]"
        sys.exit()
    AuthenticationHandler.key = base64.b64encode(sys.argv[2])
    BaseHTTPServer.test(AuthenticationHandler, BaseHTTPServer.HTTPServer)
