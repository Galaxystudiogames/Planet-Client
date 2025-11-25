import threading
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer
import minecraft_launcher_lib
import addAccount as acc


#Server Variables
host = "localhost"
port = 8080


# Http Server Config
class Auth(BaseHTTPRequestHandler,):
    # defining HTML files
    successfile = str(open("WebserverAuth/Succes.html").read())
    failfile = str(open("WebserverAuth/Fail.html").read())

    # Get Request action
    def do_GET(self, sucessfile=successfile, failfile=failfile):

        # get url parameters
        parameters = urllib.parse.parse_qsl(self.path)
        # checking if parameters has the required token
        # checking if parameters has the required token
        if parameters != "http://localhost:8080":
            self.send_response(200)
            self.send_header("Content-type", "text/html", )
            self.end_headers()
            self.wfile.write(bytes(self.successfile, "utf-8"))
            # return token
            token1 = minecraft_launcher_lib.microsoft_account.get_auth_code_from_url(url="http://localhost:8080" + self.path)
            token2 = parameters[0][1]
            #print("Token über Libary: " + token1)
            print("Token ohne Libary: " + token2)
            acc.AddAccount(token2)

        # giving an Error when no token
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html", )
            self.end_headers()
            self.wfile.write(bytes(self.failfile, "utf-8"))



#Start Http Server
def StartServer():
    server = HTTPServer((host, port), Auth)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()