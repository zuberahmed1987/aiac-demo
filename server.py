import http.server

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')

httpd = http.server.HTTPServer(('localhost', 8080), MyHTTPRequestHandler)
print('Starting server...')
httpd.serve_forever()