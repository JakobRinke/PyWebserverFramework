
from _collections import  defaultdict

import JWebServer.RequestParser.HyperArgs as HyperArgs
import __main__
import traceback
import os

config = __import__("config")
try:
    config = __main__.conf
except:
    pass



def EditSite(Website, args):



    Locked_Sites = defaultdict(lambda: 0)
    Locked_Scripts = defaultdict(lambda: 0)

    try:
        changed = True

        while changed == True:
            changed = False
            did = []



            if True:





                for Path in config.Prot:
                    if "[|" + Path + "|]" in Website and Locked_Sites[Path] <= config.IncProtection:
                        Add = ""
                        with open("./Templates/Protected/" + Path) as File:
                            for line in File:
                                Add += line + "\n"
                        Locked_Sites[Path] += 1
                        changed = True
                        Website = Website.replace("[|" + Path + "|]", "\n" + Add)
                        did.append(Path)
                    elif "[|" + Path + "|]" in Website:
                        Website = Website.replace("[|" + Path + "|]", "")

                for Path in config.Temp:
                    if "[|" + Path + "|]" in Website and Locked_Sites[Path] <= config.IncProtection and not Path in did:
                        Add = ""
                        with open("./Templates/" + Path) as File:
                            for line in File:
                                Add += line + "\n"
                            Locked_Sites[Path] += 1
                            changed = True
                        Website = Website.replace("[|" + Path + "|]", "\n" + Add)
                    elif "[|" + Path + "|]" in Website:
                        Website = Website.replace("[|" + Path + "|]", "")


               # print (config.Scripts)
                for Script in config.Scripts.keys():
                    if "{|" + Script + "|}" in Website and Locked_Scripts[Script] <= config.IncProtection:

                        try:
                            Website = Website.replace("{|" + Script + "|}", "\n" + config.Scripts[Script].run(request=args))
                        except:
                            try:
                                Website = Website.replace("{|" + Script + "|}", "\n" + config.Scripts[Script].run())

                            except:
                                pass
                        Locked_Scripts[Script] += 1
                        changed = True
                    elif "{|" + Script + "|}" in Website:
                        Website = Website.replace("{|" + Script + "|}", "")

				
                Website = HyperArgs.GetHyperArgs(Website, args,  Locked_Sites,  Locked_Scripts, config.Scripts, config.IncProtection,  config.Prot, config.Temp)




        #print("HyperArgs: " + GetHyperArgs(Website, args,  Locked_Sites,  Locked_Scripts))
    except:
        traceback.print_exc()

    return Website




def getSite(path, args={}, code=200):
    Locked_Sites = defaultdict(lambda: 0)
    Locked_Scripts = defaultdict(lambda: 0)

    Website = ""
    if os.path.relpath("./Templates" + path, "./Templates").startswith(".."):
        return GetError(404, args)


    try:
        if not str(path).endswith("/"):
            with open("./Templates" + path) as File:
                if not str(path).startswith("Protected"):
                    for line in File:
                        Website += line + "\n"

                else:
                    print("File Not found")



        else:
            with open("./Templates/" + path + "index.html") as File:
                if not str(path).startswith("Protected"):
                    for line in File:
                        Website += line + "\n"

                else:
                    print("File Not found")


        Website = EditSite(Website, args)
    except:
        try:
            with open("./Templates/" + path + "/index.html") as File:
                if not str(path).startswith("Protected"):
                    for line in File:
                        Website += line + "\n"

                else:
                    print("File Not found")

            Website = EditSite(Website, args)
        except:
            return GetError(404, args)

    return code, Website.encode("utf-8").decode("utf-8").replace("Ã¤", "ä").replace("Ã¼", "ü").replace("Ã¶", "ö").replace("ÃŸ", "ß").replace("Ã„", "Ä").replace("Ãœ", "Ü").replace("Ã–", "Ö")




def GetError(Num, args):
    if config.Error[Num] != -1:
        return getSite(config[Num], args, Num)
    else:
        return Num, "An Error occurred: " + str(Num)
