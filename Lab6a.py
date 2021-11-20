from board import LED
from machine import Pin, PWM, Timer
from time import sleep
import time
import math

#led = Pin(LED, mode=Pin.OUT)
led_ext = Pin(27, mode=Pin.OUT)
'''
brightness = 0
L1 = PWM(led_ext,freq=200,duty=brightness,timer=0)

def tcb(timer):
    global brightness
    if brightness < 100:
        brightness += 1
    else:
        brightness = 0

    print(brightness)
    L1.duty(brightness)

t1.init(period=10, mode=t1.PERIODIC, callback=tcb)
'''

C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5_ = 880
AS5 = 932
B5 = 988
C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 1245
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978

bach = [
G3,b,G3,
C4,C4,C4,C4,C4,
G4,G4,G4,G4,G4,G4,
F4,E4,D4,
C5,C5,C5,C5,C5,C5,
G4,G4,G4,
F4,E4,D4,
C5,C5,C5,C5,C5,C5,
G4,G4,G4,
F4,E4,F4,D4,D4,D4,D4,
99999,99999,99999,99999]

# C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, G4, C5, E5, G4, C5, E5,
# C4, D4, G4, D5, F5, G4, D5, F5, C4, D4, G4, D5, F5, G4, D5, F5,
# B3, D4, G4, D5, F5, G4, D5, F5, B3, D4, G4, D5, F5, G4, D5, F5,
# C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, G4, C5, E5, G4, C5, E5,
# C4, E4, A4, E5, A5_, A4, E5, A4, C4, E4, A4, E5, A5_, A4, E5, A4,
# C4, D4, FS4, A4, D5, FS4, A4, D5, C4, D4, FS4, A4, D5, FS4, A4, D5,
# B3, D4, G4, D5, G5, G4, D5, G5, B3, D4, G4, D5, G5, G4, D5, G5,
# B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5,
# B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5,
# A3, C4, E4, G4, C5, E4, G4, C5, A3, C4, E4, G4, C5, E4, G4, C5,
# D3, A3, D4, FS4, C5, D4, FS4, C5, D3, A3, D4, FS4, C5, D4, FS4, C5,
# G3, B3, D4, G4, B4, D4, G4, B4, G3, B3, D4, G4, B4, D4, G4, B4
# ]

start = 0
L1 = PWM(led_ext,freq=bach[0],duty=50,timer=0)

def speaker(timer):
    global note
    global start
    note = bach[start]
    print(note)
    L1.freq(note)
    if start < len(bach)-1:
        start += 1
    else:
        start = 0

t1 = Timer(0)
t1.init(period= 200, mode=t1.PERIODIC, callback=speaker)

#led_ext = Pin(LED, mode=Pin.OUT)
