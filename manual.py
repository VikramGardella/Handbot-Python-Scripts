from __future__ import division
import RPi.GPIO as gpio
import time
import curses
from adafruit_servokit import ServoKit

kit = ServoKit(channels = 16)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

for i in range(16):
    kit.servo[i].angle = 90

#kit.servo[x].set_pulse_width_range(min, max)

limb_names = ['wrist', 'thumb', 'fore', 'middle', 'ring', 'pinky']
limb_motor_channels = [[0, 1], [15, 10], [14, 9, 5], [13, 8, 4], [12, 7, 3], [11, 6, 2]]
limb_index = 0

#for i in range(16):
#    kit.servo[i].angle = 90

try:
    while True:
        char = screen.getch()
        if(char != -1):
            #knuckle tests
            if(char == ord(';')):
                print('pinky knuckle - mid position')
                kit.servo[0].angle = 150
                #break
            else:
                kit.servo[0].angle = 30
            if(char == ord('l')):
                print('ring finger')
                kit.servo[1].angle = 150
                #break
            else:
                kit.servo[1].angle = 30
            if(char == ord('k')):
                print('middle finger')
                kit.servo[2].angle = 150
                #break
            else:
                kit.servo[2].angle = 30
            if(char == ord('j')):
                print('fore finger knuckle - mid')
                kit.servo[3].angle = 150
                #break
            else:
                kit.servo[3].angle = 30
            if(char == ord('h')):
                print('thumb knuckle - mid')
                kit.servo[4].angle = 30
                #break
            else:
                kit.servo[4].angle = 150

            #wrist tests
            if(char == ord('a')):
                print('wrist rotate - mid')
                #will use channel: kit.servo[14]
                kit.servo[14].angle = 20
                #break
            else:
                kit.servo[14].angle = 90
            if(char == ord('s')):
                print('wrist flip - mid')
                #will use channel: kit.servo[15]
                kit.servo[15].angle = 150
                #break
            else:
                kit.servo[15].angle = 60
                print('Clean signal to servo driver here.')

            time.sleep(0.1)

except KeyboardInterrupt:
    terminate()

finally:
    terminate()

