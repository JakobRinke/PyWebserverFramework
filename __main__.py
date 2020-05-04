


print("Lade Config ...\n")

import config
config.load()
conf = config

print("\nConfig wurde geladen\n\n")




print("Starte Initialisieren des Servers ...\n")
import  JWebServer


Server = JWebServer.JHTTPServer()
print("\nServer wurde Initialisiert\n\n")


print("\n\n Server Einsatzbereit ...")
Server.start_server()