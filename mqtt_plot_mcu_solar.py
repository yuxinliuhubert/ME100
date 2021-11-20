from mqttclient import MQTTClient
from math import sin
import network
import sys
from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
import time

"""
Send measurement results from microphyton board to host computer.
Use in combination with mqtt_plot_host.py.

'print' statements throughout the code are for testing and can be removed once
verification is complete.
"""

# Important: change the line below to a unique string,
# e.g. your name & make corresponding change in mqtt_plot_host.py
session = 'hubert/ESP32/helloworld'
BROKER = 'broker.mqttdashboard.com'

# check wifi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == '0.0.0.0':
    print("no wifi connection")
    sys.exit()
else:
    print("connected to WiFi at IP", ip)

# connect to MQTT broker
print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = MQTTClient(BROKER, port='1883')
print("Connected!")

i2c = I2C(id=0, scl=Pin(SCL), sda=Pin(SDA), freq=100000)
# send data
# In this sample, we send "fake" data. Replace this code to send useful data,
# e.g. measurement results.
print("scanning I2C bus ...")
print("I2C:", i2c.scan())
above = False

SHUNT_RESISTOR_OHMS = 0.1
ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
ina.configure()
while above == False:
    time.sleep(0.3)
    i = ina.current()
    v = ina.voltage()
    r = 0;
    if i != 0:
        r = 1000* v/i
    p = ina.power()/1000
    print("Current is ",i)
    print("Voltage is ",v)
    print("Resistance is ",r)
    #
    # print("Power is ",ina.power()/1000)
    # add additional values as required by application
    if r <= 800:
        topic = "{}/data".format(session)
        data = "{},{},{},{}".format(v,i,p,r)
        print("send topic='{}' data='{}'".format(topic, data))
        mqtt.publish(topic, data)
    if r > 800:
        above = True;

# do the plotting (on host)
print("tell host to do the plotting ...")
mqtt.publish("{}/plot".format(session), "create the plot")

# free up resources
# alternatively reset the microphyton board before executing this program again
mqtt.disconnect()
