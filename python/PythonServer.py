from HubRequestHandler import HubRequestHandler 
from http.server import HTTPServer
from packages.pythonhub import PythonHub


class PythonServer:
    def __init__(self, host='localhost', port=8080):
        self.port = port
        self.host = host
        self.server = HTTPServer((self.host, self.port), HubRequestHandler)
        self.server.gateway = PythonHub()
    
    def __del__(self):
        self.server.socket.close()
        print("Server is closed")
        
    def run(self):
        print("Server is running on", self.host, ":", self.port)
        self.server.serve_forever()
        
    def stop(self):
        self.server.shutdown()
        self.server.socket.close()
        print("Server is closed")
