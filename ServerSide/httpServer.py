# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from serverDef import html, hostName, serverPort
from serverDef import globalVars
from urllib.parse import urlparse
from urllib.parse import parse_qs
from cameraFunc import maviAlgila
import threading

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html, "utf-8"))
        parsed_url = urlparse(self.path)
        captured_value = parse_qs(parsed_url.query)
        if(captured_value):
            if('sliderLhue' in parsed_url.path):
                globalVars.oHueL = captured_value['value'][0]
            elif('sliderLsat' in parsed_url.path):
                globalVars.oSatL = captured_value['value'][0]
            elif('sliderLval' in parsed_url.path):
                globalVars.oValL = captured_value['value'][0]
            elif('sliderHhue' in parsed_url.path):
                globalVars.oHueH = captured_value['value'][0]
            elif('sliderHsat' in parsed_url.path):
                globalVars.oSatH = captured_value['value'][0]
            elif('sliderHval' in parsed_url.path):
                globalVars.oValH = captured_value['value'][0]
            elif('sliderMker' in parsed_url.path):
                globalVars.oMker = captured_value['value'][0]
            elif('sliderGker' in parsed_url.path):
                globalVars.oGker = captured_value['value'][0]
            elif('sliderOpay' in parsed_url.path):
                globalVars.oOpay = captured_value['value'][0]
            globalVars.isNew = True
    
    def log_message(self, format, *args):
        return

def serverThread():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
def cameraThread():
    while True:
      maviAlgila()

def runAll():
    server = threading.Thread(target=serverThread)
    camera = threading.Thread(target=cameraThread)
    server.start()
    camera.start()