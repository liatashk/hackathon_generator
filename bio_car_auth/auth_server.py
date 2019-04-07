#!/usr/bin/env python3
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from send_to_canvas import start_engine


PORT_NUMBER = 80
HOST_NAME = '192.168.100.198'


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/auth': {'status': 200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        content = ""
        if status_code == 200:
            start_engine()
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            content = '''
            <html><head><title>Welcome to auth server.</title></head>
            <body><p>Success Auth!</p>
            <p>You accessed path: {}</p>
            </body></html>
            '''.format(path)
            return bytes(content, 'UTF-8')
        else :
            content= "bad request"
            return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)


def main():
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
    

if __name__ == "__main__":
    main()

