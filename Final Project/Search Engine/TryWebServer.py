from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8000


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('<script async src="https://cse.google.com/cse.js?cx=30def17c2d9c73cb8"></script>', "utf-8"))
        self.wfile.write(bytes('<div class="gcse-search"></div>', "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server Closed")