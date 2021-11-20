from board import LED
import PWM
from machine import Pin
import time
#Initialize built in LED Pin
led = Pin(14, mode = Pin.OUT)


for i in range(1,300000):
    led(1)
    time.sleep(0.002)
    led(0)
    time.sleep(0.002)
