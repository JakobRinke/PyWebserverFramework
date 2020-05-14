import os
import sys


try:
	from pynput import  keyboard
except:
	os.system("py -3 -m pip install pynput")
	os.system("python -m pip install pynput")
	from pynput import keyboard
	
import subprocess
import time
from threading import Thread

class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()

process = subprocess.Popen(['call',"start.bat"],shell = True, stdout=sys.stdout, stderr=sys.stdout, stdin=subprocess.PIPE)

process.kill()


def on_activate():
	try:
		print('Global hotkey activated!')
		try: 
			process.kill()
		except:
			pass
		
		process = subprocess.Popen(['call',"start.bat"],shell = True)
	except:
		pass
	
	return
	
   

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+b'),
    on_activate)
	
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
	
while True:

    time.sleep(1000)