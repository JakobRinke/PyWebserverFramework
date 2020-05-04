
from http.server import BaseHTTPRequestHandler

from JWebServer.DefFunc import FileHandleFuncs as Functions


import JWebServer.RequestParser as rp










class MainRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):
        self.ParseArgs()

        if self.path.endswith(".png") or self.path.endswith(".gif") or self.path.endswith(".jpg"):
            self.SendImage("Templates/" + self.path)
        else:
            Code, Site = rp.getSite(path=self.path, args=self.args)
            self.SendResult(status=Code, Website=Site)

    def do_POST(self):

        length = self.headers["content-length"]
        s = self.rfile.read(int(length))
        self.args = {}
        try:
            for arg in str(s).split("&"):
                self.args[str(arg.split("=")[0]).replace("b'","").replace("'","")] = str(arg.split("=")[1]).replace("-b'","").replace("'","")

        except:
            pass

        if self.path.endswith(".png") or self.path.endswith(".gif") or self.path.endswith(".jpg"):
            self.SendImage("Templates/" + self.path)
        else:
            Code, Site = rp.getSite(path=self.path, args=self.args)
            self.SendResult(status=Code,Website=Site)




    def ParseArgs(self):
        self.args = {}
        try:
            for arg in str(self.path).split("?")[1].split("&"):
                self.args[arg.split("=")[0]] = arg.split("=")[1]
            self.path = str(self.path).split("?")[0]
        except:
            pass

    def SendResult(self,status=200, Website="", encoding="utf-8" ):
        self.send_response(status)
        self.SendDefHeaders(encoding=encoding)
        self.wfile.write(str(Website).encode("utf-8"))


    def SendImage(self, File=""):
        Image = Functions.load_binary(File)
        self.send_response(200)
        self.send_header('Content-type', 'image/' + File[-3:])
        self.end_headers()
        self.wfile.write(Image)





    def SendDefHeaders(self, encoding="utf-8"):
        self.send_header('Content-type', 'text/html; charset=' + encoding)
        self.end_headers()

