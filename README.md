
# JPyFramework
Einfacher Webserver für Python Entwickler



<h2> Inhalt </h2>
<a href="#1" style="color: black;"> 1. Installation </a><br><br>
<a href="#2" style="color: black;"> 2. Starten </a> <br>
<a href="#2.1" style="color: black;"> 2.1 Windows </a> <br>
<a href="#2.2" style="color: black;"> 2.2 Mac </a>  <br><br>
<a href="#3" style="color: black;"> 3. Verbinden </a> <br><br>
<a href="#4" style="color: black;"> 4. Website erstellen </a> <br><br>
<a href="#5" style="color: black;"> 5. Website einfügen </a> <br><br>
<a href="#6" style="color: black;"> 6. Python Scripts Einfügen </a> <br><br>
<a href="#7" style="color: black;"> 7. Formulare mit Python </a> <br><br>
<a href="#8" style="color: black;"> 8. HyperArgs </a> <br>
<a href="#8.1" style="color: black;"> 8.1 Warum Hyperargs </a> <br>
<a href="#8.2" style="color: black;"> 8.2 Einbinden in Python </a> <br>
<a href="#8.3" style="color: black;"> 8.3 Aufrufen in HTML </a> <br><br>

<hr>

<h2 id="1"> 1 Installation </h2>

Damit der Webserver funktioniert, muss die neuste Version von Python 3 installiert sein. 
Diese kann ist <a href="https://www.python.org/downloads/">hier</a> verfügbar.
Danach muss man sich nur noch die neuste Version dieses Webservers herunterladen und entpacken.
<br><br><br>

<h2 id="2"> 2 Starten </h2>

<h3 id="2.1"> 2.1 Windows </h3> <br>
1. Öffne die start.bat
<br>
<br>
2. Ein Konsolenfenster sollte sich öffnen und folgende Meldungen anzeigen:
<br>
<img src="https://githubbilderjakob.000webhostapp.com/PyWebserver/Start_Windows_Cmd.png" width="100%">
3. Der Webserver wurde erfolgreich gestartet
<br>
<br> 
4. Um ihn zu beenden, schließe einfach das Konsolenfenster
<br>
<br> 
<br>
<h3 id="2.2"> 2.2 Mac </h3> <br>
1. Drücke Rechtsklick auf die start.sh, öffnen mit, wähle alle Programme aus, 
aktiviere immer öffnen mit und suche nach dem Programm Terminal.
<br>
<br>
2. Ein Konsolenfenster sollte sich öffnen und folgende Meldungen anzeigen (Das aussehen des Fensters kann anders aussehen):
<br>
<img src="https://githubbilderjakob.000webhostapp.com/PyWebserver/Start_Windows_Cmd.png" width="100%">
3. Der Webserver wurde erfolgreich gestartet
<br>
<br> 
4. Um ihn zu beenden, schließe einfach das Konsolenfenster
<br>
<br> 
<br>

<h2 id="3"> 3 Verbinden mit dem Webserver </h2>
Wenn der Server sich gestartet hat, kann man sich mit der Url: <a href="http://localhost">localhost</a> zu verbinden 
<br>
<br> 
<br>

<h2 id="4"> 4 Erstellen einer Website </h2>
Jede HTML Komponente der Website muss in den Templates Ordner. Um eine Start Website zu erstellen muss man eine index.html datei im Templates Ordner erstellen. Wenn man jetzt Schritt 3 erneut ausführt (sich neu Verbindet) wird die Index Datei angezeigt. Wenn das nicht sofort klappt muss man den Webserver neu laden
<br>
<br> 
<br>

<h2 id="5"> 5 Websites ineinander einfügen </h2>
1. Erstelle eine neue html Datei im Templates/Protected Ordner. Schreibe einen Bespieltext in diese Website. Auf diese Website kann niemand direkt zugreifen.
<br>
<br>
2. Schreibe [|NAME|] in deine index Datei, wobei du das NAME durch den Namen der Datei ersetzt, die in Schritt 1 erstellt wurde (mit Dateiendung).
<br>
<br>
3. Wenn man die Website jetzt neulädt, wird der [|NAME|] Aufruf durch den Inhalt der im Protected Ordner liegenden Website ausgetauscht
<br>
<br>
4. Einen solchen Aufruf kann man mehrmals in einer Website und auch mit verschieden Websites tätigen
<br>
<br>
<br>
<h2 id="6"> 6 Python Scripts Einfügen </h2>
1. Erstelle ein Python Script mit einer run Methode, in der ein String zurückgegeben wird
<br>
<br>
2. Schreibe [|NAME|] in deine index Datei, wobei du das NAME durch den Namen des Scripts ersetzt, die in Schritt 1 erstellt wurde (ohne Dateiendung) und starte den Webserver neu.
<br>
<br>
3. Wenn man die Website jetzt neulädt, wird der [|NAME|] Aufruf durch den Inhalt die Rückgabe der run Methode ersetzt
<br>
<br>
4. Einen solchen Aufruf kann man mehrmals in einer Website und auch mit verschieden Scripts tätigen
<br>
<br>
<br>

<h2 id="7"> 7 Formulare Weitergeben </h2>
Egal ob Get oder Post, alle Formulardaten können von einem Script abgefangen werden. Hierzu muss nur ein Parameter Request ind der run methode erstellt werden. Die Formulardaten werden dann als Dictionary an den requestparameter weitergeben und können von dem Script benutzt werden. zum testen muss der Server neu gestartet werden

<br>
<br>
<br>

<h2 id="8"> 8 Hyper Args </h2>

<h3 id="8.1"> 8.1 Was ist HyperArgs? </h3> <br>
Angenommen man schreibt ein Script, welches Bilder aus einen Ordner ausließt und diese dann mit einem Image Tag aufruft. Jetzt will man dieses Script aber für 2 Verschiede Ordner auf 2 Verschiedenen Websites ausführen. Wenn man nicht zwei Scripts schreiben möchte, sind HyperArgs die Lösung. Hyper Args bietet die Möglichkeit, Parameter über den Html Code an Python Scripts zu übergeben.
<br>
<br>
<h3 id="8.2"> 8.2 Einbindung in das Script </h3> <br>
Um Hyper Args zu einem Script hinzuzufügen, muss man einen weiteren Parameter  hyper = {}   erstellen. Dieses Dictionary enthält alle Daten die über HyperArgs übergeben werden.
<br><br>
<h3 id="8.3"> 8.3 Aufrufen in HTML </h3> <br>
Die Einbindung funktioniert zunächst wie eine normale Einbindung (  {|SCRIPT|}  ). Die Einbindung hier funktioniert so: <br>
<h5> {|SCRIPT?PARAMETER1=WERT1&PARAMETER2=WERT2&PARAMETER3=WERT3|} </h5>

