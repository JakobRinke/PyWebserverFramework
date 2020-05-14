from _collections import  defaultdict



changed = False

def GetHyperArgs (Website, args, Locked_Sites,  Locked_Scripts, Scripts, IncMax, Prot ,Sites):
    LockedArgs = defaultdict(lambda: 0)
    changed = True
	
    while changed == True:
        changed = False
		try:
            Website, Locked_Scripts = GetHyperArgsScript(Website, Locked_Scripts, IncMax, args, Scripts)
            Website, Locked_Sites = GetHyperArgsProt(Website, Locked_Sites, IncMax,  Prot)
            Website, Locked_Sites = GetHyperArgsWebsite(Website, Locked_Sites, IncMax, Sites)
            Website, LockedArgs = GetRequestArgs(Website,IncMax, args, LockedArgs)
		except:
			pass
    return Website




def GetHyperArgsScript(Website, Locked_Scripts, IncMax, args, Scripts):
    for Script in Scripts.keys():

        Replace = ""
        Hyper = {}
        if ("{|" +Script) in Website and Locked_Scripts[Script] <= IncMax:
            tmp = Website.split("{|" + Script)[1].split("|}")[0]
            Replace = "{|" + Script + tmp + "|}"
            if tmp[0] == "?":
                tmp = tmp[1:]
                for t in tmp.split("&"):
                    try:
                        Hyper[t.split("=")[0].strip()] = t.split("=")[1].strip()
                    except:
                        pass



        if Hyper != {}:

            try:
                Website = Website.replace(Replace, "\n" + Scripts[Script].run(request=args, hyper = Hyper))

            except:
                try:
                    Website = Website.replace(Replace, "\n" + Scripts[Script].run(hyper = Hyper))


                except Exception as e:
                    print("Script Error in Script " + Script + ": " + e)
            Locked_Scripts[Script] += 1
            changed = True
        elif Replace in Website:
            Website = Website.replace("{|" + Script + "|}", "")
            changed = True



    return Website, Locked_Scripts



def GetHyperArgsWebsite(Website, Locked_Sites, IncMax, Prot):
    for Path in Prot:

        Replace = ""
        Hyper = {}
        if ("[|" + Path) in Website and Locked_Sites[Path] <= IncMax:
            tmp = Website.split("[|" + Path)[1].split("|]")[0]
            Replace = "[|" + Path + tmp + "|]"

            if tmp[0] == "?":
                tmp = tmp[1:]
                for t in tmp.split("&"):
                    try:
                        Hyper[t.split("=")[0].strip()] = t.split("=")[1].strip()
                    except:
                        pass





        if Hyper != {}:
            Add = ""

            with open("./Templates/" + Path) as File:
                for line in File:
                    Add += line + "\n"

            Locked_Sites[Path] += 1

            for i in Hyper.keys():
                Add = Add.replace("(|" + i + "|)", Hyper[i])

            Website = Website.replace(Replace, "\n" + Add)
            changed = True
        elif Replace in Website:
            Website = Website.replace(Replace, "")
            changed = True

    return Website, Locked_Sites




def GetHyperArgsProt(Website, Locked_Sites, IncMax, Prot):
    for Path in Prot:

        Replace = ""
        Hyper = {}
        if ("[|" + Path) in Website and Locked_Sites[Path] <= IncMax:
            tmp = Website.split("[|" + Path)[1].split("|]")[0]
            Replace = "[|" + Path + tmp + "|]"

            if tmp[0] == "?":
                tmp = tmp[1:]
                for t in tmp.split("&"):
                    try:
                        Hyper[t.split("=")[0].strip()] = t.split("=")[1].strip()
                    except:
                        pass





        if Hyper != {}:
            Add = ""

            with open("./Templates/Protected/" + Path) as File:
                for line in File:
                    Add += line + "\n"

            Locked_Sites[Path] += 1

            for i in Hyper.keys():
                Add = Add.replace("(|" + i + "|)", Hyper[i])

            Website = Website.replace(Replace, "\n" + Add)
            changed = True
        elif Replace in Website:
            Website = Website.replace(Replace, "")
            changed = True
    return Website, Locked_Sites






def GetRequestArgs(Website,inc, args = {}, LockedArgs = {}):
    for key, value in args.items() :
        if LockedArgs[key] < inc:
            Website = Website.replace("(-" + str(key) + "-)",  str(value))
            LockedArgs[key] += 1
            changed = True

    return Website, LockedArgs



def GetWebsite (Path):
    Website = ""
    with open("./Templates/" + Path) as File:
        for line in File:
            Website += line + "\n"
    return Website



print("Hyper Args imported")