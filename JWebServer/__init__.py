import __main__
from http.server import HTTPServer
import JWebServer.RequestHandler as JServer
from socketserver import ThreadingMixIn

import ssl


config = __import__("config")
try:
    config = __main__.conf
except:
    pass


class _ThreadingHttpServer(ThreadingMixIn, HTTPServer):
    pass




class JHTTPServer:

    def __init__(self, ssl=""):
        self.http_server = _ThreadingHttpServer(config.address, JServer.MainRequestHandler)
        https_server = 0
        if ssl != "":
            self.https_server.socket = _ThreadingHttpServer(config.ssladdress, JServer.MainRequestHandler)
            self.https_server.socket = ssl.wrap_socket(self.https_server.socket, certfile=ssl, server_side=True)




    def start_server (self):
        self.http_server.serve_forever()
        if self.https_server != 0:
            self.https.server_forever()
