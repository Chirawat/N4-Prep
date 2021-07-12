# Complete project details at https://RandomNerdTutorials.com

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import dht

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Phonehotspot'
password = 'hotspotpassword'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
d = dht.DHT22( Pin(12) )
Y1 = Pin(5, Pin.OUT)
Y2 = Pin(4, Pin.OUT)
Y1.off()
Y2.off()

