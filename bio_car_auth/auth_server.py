#!/usr/bin/env python3
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from send_to_canvas import start_engine


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/auth': {'status': 200}
        }
        print("Got new connection from:" + str(self.client_address[0]) + ":" + str(self.client_address[1]))
        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        content = ""
        if status_code == 200:
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = '''
            <html><head><title>Welcome to auth server.</title></head>
            <body><p>Success Auth!</p>
            <p>going to run enigne...</p>
            </body></html>
            '''
            print("Going to start engine...")
            start_engine()
            return bytes(content, 'UTF-8')
        else :
            content= "bad request"
            return bytes(content, 'UTF-8')

    def respond(self, opts): 
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)


def runServer(ipAddr, port=80):
    server_class = HTTPServer
    httpd = server_class((ipAddr, port), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (ipAddr, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (ipAddr, port))
    
def usage():
    print("Please run as follow:")
    print("python auth_server.py <ipAddr> <port>")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(1)
        
    if len(sys.argv) >= 3:
        runServer(sys.argv[1], sys.argv[2])
    else:
        runServer(sys.argv[1])

