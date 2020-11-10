import os
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

os.chdir(r'C:\Users\iwost\Desktop\Rekrutacja') #open proper directory
server = HTTPServer(("",8888), SimpleHTTPRequestHandler) 
server.serve_forever() #opens a server