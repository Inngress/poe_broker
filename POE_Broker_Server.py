from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests as rq
import json

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.sendresponse(200)
            self.sendheader("Content-type", "text/html")
            self.endheaders()
            with open('POE_Broker_Front.html', 'r') as file:
                self.wfile.write(bytes(file.read(), "utf-8"))

        elif self.path == '/api':
            gem_url = 'https://poe.ninja/api/data/itemoverview?league=Settlers&type=SkillGem'
            gem_res = rq.get(gem_url)
            gem_res_dict = gem_res.json()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # CORS header
            self.end_headers()

            self.wfile.write(bytes(json.dumps(gem_res_dict), "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>", "utf-8"))
        
        
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
