from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests as rq
import json

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        gem_url = 'https://poe.ninja/api/data/itemoverview?league=Settlers&type=SkillGem'
        gem_res = rq.get(gem_url)
        gem_res_dict = gem_res.json()
        
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("This is an example web server.", "utf-8"))
        # self.wfile.write(bytes(f"<p>{gem_res}</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")