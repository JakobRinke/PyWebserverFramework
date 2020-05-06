
from http.server import BaseHTTPRequestHandler

from JWebServer.DefFunc import FileHandleFuncs as Functions


import JWebServer.RequestParser as rp

import re








class MainRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):
        self.ParseArgs()

        if self.path.endswith(".png") or self.path.endswith(".gif") or self.path.endswith(".jpg"):
            self.SendImage("Templates/" + self.path)
        else:
            Code, Site = rp.getSite(path=self.path, args=self.args)
            self.SendResult(status=Code, Website=Site)

    def do_POST(self):

        #length = self.headers["content-length"]
        #s = self.rfile.read(int(length))
        s = ""
        self.args = {}
        type = self.headers["Content-Type"]

        if "multipart/form-data" in type.split("; ")[0]:
            args = self.HandleFile( type.split("; ")[1].split("=")[1].encode())
        else:
            len = int(self.headers["Content-Length"])
            s = self.rfile.read(len)


        try:
            if s!="":
                for arg in str(s).split("&"):
                    self.args[str(arg.split("=")[0]).replace("b'","").replace("'","")] = str(arg.split("=")[1]).replace("-b'","").replace("'","")

        except Exception as e:
            print(e)


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



    def HandleFile(self, boundary):


        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)
        if not boundary in line:
            print("No Boundary")
            return "no boundary"

        args = {}
        next = ""
        all = "".encode()
        while remainbytes > 0:

            line = self.rfile.readline()
            remainbytes -= len(line)
            if line.decode()=="":
                pass

            elif line.decode().startswith("Content"):
                if line.decode().startswith("Content-Disposition"):
                    next = line.decode().replace('Content-Disposition: form-data; name="', '').replace('"; filename=""\r\n', '').split("\"")[0]


            elif boundary in line:
                #preline = line[0:-1]
                if line.decode().endswith('\r'):
                    line = line[0:-1]
                #all += line.decode()

                args[next] = all[2:-2]
                all = "".encode()

                next = ""
            elif line.decode != "\r\n":

                all += line



        return args
