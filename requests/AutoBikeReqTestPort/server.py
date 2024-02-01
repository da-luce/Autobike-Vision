from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = self.rfile
        #message = "Hello, World! Here is a POST response"
        #self.wfile.write(bytes(message, "utf8"))
        print(message.read(20).decode("utf-8"))
        self.wfile.write(message.read(20))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()