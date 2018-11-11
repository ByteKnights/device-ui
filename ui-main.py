import driver
import math

from pynput.keyboard import Key, Listener

device_name = '/dev/ttyACM6'
width = 20
height = 4

text = []
curPos = 1

screen = driver.Driver(device_name, width, height)
screen.configSize(width, height)
screen.blinkCursor(True)
screen.clear()

def whipe():
    text = []
    curPos = 1;
    screen.clear()

def update():
    screen.clear()
    screen.println(text)
    screen.setCursor(curPos % 20, math.trunc(curPos))

def on_press(key):
    if key == Key.space:
        text.append(' ')
        curPos = 1
        update()
    elif key == Key.backspace:
        if len(text) > 0:
            del text[len(text)-1]
            curPos = 1
            update()
    elif key == Key.shift or key == Key.ctrl:
        print(key)
    if key == Key.esc:
        
    else:
        text.append(key.char)
        curPos = 1
        update()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
