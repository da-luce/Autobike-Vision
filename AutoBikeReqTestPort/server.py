from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_PUT(self):
        print("wORKINGGGGG")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = self.rfile
        #message = "Hello, World! Here is a POST response"
        #self.wfile.write(bytes(message, "utf8"))
        print(message)
        self.wfile.write(message.read(20))
        print("WORKING")

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()