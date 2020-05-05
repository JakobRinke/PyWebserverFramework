





from JWebServer.DefFunc import FileHandleFuncs as fhf
from _collections import defaultdict
import os
import time
from threading import Thread
#           Server     Port
address = ("127.0.0.1", 80)
ssladdress = ("127.0.0.1", 443)


certi =""


Scripts = {}

IncProtection = 5
reload = 5

Temp = []
Prot = []

Error = defaultdict(lambda: -1)

def load():

    global  Temp
    global  Prot
    global IncProtection
    global reload
    global Scripts
    global address
    global ssladdress
    global  certi
    global Error

    Temp = []
    Prot = []

    if not os.path.exists("./config"):
        os.mkdir("./config")

    if not os.path.exists("./Scripts"):
        os.mkdir("./Scripts")

    if not os.path.exists("./Templates"):
        os.mkdir("./Templates")

    if not os.path.exists("./Templates/Protected"):
        os.mkdir("./Templates/Protected")

    if not os.path.exists("./config/config.txt"):
        with open("./config/config.txt", "w+") as File:
            File.write("reload=5\ninception-help=5\nport=80\nsslport=80\nsslcerti=")


    if not os.path.exists("./config/error.txt"):
        with open("./config/error.txt", "w+") as File:
            File.write("\n")


    config = {}

    with open("./config/config.txt") as File:
        for l in File:
            try:
                l = l.replace("\n", "")
                name = l.split("=")
                config[name[0].strip()] = name[1].strip()
            except:
                pass

    with open("./config/error.txt") as File:
        for l in File:
            try:
                l = l.replace("\n", "")
                name = l.split("=")
                Error[int(name[0].strip())] = name[1].strip()
            except:
                pass

    try:
        IncProtection = int(config["inception-help"])
        if IncProtection < 1:
            IncProtection = 5
    except:
        IncProtection=5

    try:
        port = int(config["port"])
        address=("127.0.0.1", port)
    except:
        address=("127.0.0.1", 80)

    try:
        port = int(config["sslport"])
        ssladdress=("127.0.0.1", port)
    except:
        ssladdress=("127.0.0.1", 443)

    try:
        certi = config["sslcerti"]
    except:
        certi=""


    scripts = fhf.getListOfFiles("./Scripts", ".py")
    for Script in scripts:
        try:
            Script = Script.replace("\n", "").replace(".py","").replace("./Scripts\\","")
          
            Scripts[Script] = fhf.imp("Scripts." + Script)
            print("Eigenes Script gefunden:  " + Script)
        except Exception as e:		
            print("Fehler beim Script  " + Script + "   :")
            print(e)



    for f in fhf.getListOfFiles("./Templates/Protected"):
        Prot.append(os.path.relpath(f, "./Templates/Protected").replace("\\", "/"))


    for f in fhf.getListOfUnprotFiles("./Templates"):
        Temp.append(os.path.relpath(f, "./Templates").replace("\\", "/"))


    if reload<0:
        Thr = Thread(target=Reload, args=(reload))
        Thr.start()


def Reload(sleep=5):
    while True:
        time.sleep(sleep)
        global Prot
        global Temp

        for f in fhf.getListOfFiles("./Templates"):
            Temp.append(os.path.relpath(f, "./Templates").replace("\\", "/"))

        for f in fhf.getListOfFiles("./Templates/Protected"):
            Prot.append(os.path.relpath(f, "./Templates/Protected").replace("\\", "/"))




