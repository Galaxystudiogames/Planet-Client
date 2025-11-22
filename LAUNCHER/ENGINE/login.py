import pathlib
import webbrowser
import minecraft_launcher_lib
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import subprocess
import sys




#Login
def Login():

    #Azure Stuff
    CLIENT_ID = "01cabc92-07d5-445d-9bde-0d43161fc331"
    REDIRECT_URL = "http://localhost:8080"

    # Login
    login_url, state, code_verifier = minecraft_launcher_lib.microsoft_account.get_secure_login_data(CLIENT_ID,REDIRECT_URL)
    webbrowser.open_new(url=login_url)
    StartServer()



#Http Server Config
class Auth(BaseHTTPRequestHandler):
    # defining HTML files
    successfile = str(open("WebserverAuth/Succes.html").read())
    failfile = str(open("WebserverAuth/Fail.html").read())

    # Get Request action
    def do_GET(self, sucessfile=successfile, failfile=failfile):

        #get url parameters
        parameters = urllib.parse.parse_qsl(self.path)

        #checking if parameters has the required token
        if str(parameters) != "[]":
            self.send_response(200)
            self.send_header("Content-type", "text/html", )
            self.end_headers()
            self.wfile.write(bytes(self.successfile, "utf-8"))
            #return token
            token = parameters[0][1]
            print(token)

        #giving an Error when no token
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html", )
            self.end_headers()
            self.wfile.write(bytes(self.failfile, "utf-8" ))



#Server Variables
host = "localhost"
port = 8080



#Start Http Server
def StartServer():
    server = HTTPServer((host, port), Auth)
    server.serve_forever()


#Stopping Http Server
def ServerStop():
    server = HTTPServer((host, port), Auth)
    server.shutdown()
    server.server_close()



Login()