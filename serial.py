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

#middle and bottom apparent optimal range:
#[700, 1800] = 180 degree range approx.
#[800, 1400] so 1100 is mid angle

limb_names = ['wrist', 'thumb', 'fore', 'middle', 'ring', 'pinky']
limb_motor_channels = [[0, 1], [15, 10], [14, 9, 5], [13, 8, 4], [12, 7, 3], [11, 6, 2]]
limb_index = 0

#top_motor_angs = [90, 90, 90, 90]
#mid_motor_angs = [90, 90, 90, 90]
#bot_motor_angs = [90, 90, 90, 90]

for i in range(16):
    kit.servo[i].angle = 90

try:
    while True:
        char = screen.getch()
        if(char != -1):
            #switch leg to manipulate
            if(char == ord('u')):
                limb_index = 0
                print('Now controlling front left leg.')
            elif(char == ord('i')):
                limb_index = 1
                print('Now controlling front right leg.')
            elif(char == ord('j')):
                limb_index = 2
                print('Now controlling back left leg.')
            elif(char == ord('k')):
                limb_index = 3
                print('Now controlling back right leg.')

            #knuckle tests
            elif(char == ord('a')):
                print('pinky knuckle - mid position')
            elif(char == ord('s')):
                print('top motor angle middle')
                kit.servo[limb_motor_channels[limb_index][0]].angle = 90
            elif(char == ord('d')):
                print('top motor angle add')
            elif(char == ord('f')):
                print('fore knuckle - mid')
            elif(char == ord('g')):
                print('thumb knuckle - mid')

            #wrist tests
            elif(char == ord('u')):
                print('wrist rotate - mid')
            elif(char == ord('i')):
                print('wrist flip - mid')

            elif(char == ord('t')):
                print('setting motor positions for installing top limbs')
                time.sleep(0.003)
                kit.servo[limb_motor_channels[0][0]].angle = 145
                time.sleep(0.003)
                kit.servo[limb_motor_channels[1][0]].angle = 45
                time.sleep(0.003)
                kit.servo[limb_motor_channels[2][0]].angle = 45
                time.sleep(0.003)
                kit.servo[limb_motor_channels[3][0]].angle = 145
            elif(char == ord('o')):
                time.sleep(0.003)
                kit.servo[limb_motor_channels[0][0]].angle = 55
                time.sleep(0.003)
                kit.servo[limb_motor_channels[1][0]].angle = 135
                time.sleep(0.003)
                kit.servo[limb_motor_channels[2][0]].angle = 135
                time.sleep(0.003)
                kit.servo[limb_motor_channels[3][0]].angle = 55
                print('legs out')
            elif(char == ord('p')):
               kit.servo[limb_motor_channels[0][0]].angle = 100
               kit.servo[limb_motor_channels[1][0]].angle = 90
               kit.servo[limb_motor_channels[2][0]].angle = 90
               kit.servo[limb_motor_channels[3][0]].angle = 100
            elif(char == ord('y')):
                print('make mid motors max position')
                kit.servo[limb_motor_channels[0][1]].angle = 145
                kit.servo[limb_motor_channels[1][1]].angle = 45
                kit.servo[limb_motor_channels[2][1]].angle = 45
                kit.servo[limb_motor_channels[3][1]].angle = 145
            elif(char == ord('h')):
                print('make mid motors middle')
                kit.servo[limb_motor_channels[0][1]].angle = 100
                kit.servo[limb_motor_channels[1][1]].angle = 90
                kit.servo[limb_motor_channels[2][1]].angle = 90
                kit.servo[limb_motor_channels[3][1]].angle = 100
            elif(char == ord('n')):
                print('make mid motors min position')
                kit.servo[limb_motor_channels[0][1]].angle = 55
                kit.servo[limb_motor_channels[1][1]].angle = 135
                kit.servo[limb_motor_channels[2][1]].angle = 135
                kit.servo[limb_motor_channels[3][1]].angle = 55
            else:
                print('Clean signal to servo driver here.')

        #time.sleep(0.001)

except KeyboardInterrupt:
    terminate()

finally:
    terminate()

