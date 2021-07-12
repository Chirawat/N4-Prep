try:
  import usocket as socket
except:
  import socket

from machine import Pin, I2C
import network
import dht
import ssd1306

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

i2c = I2C(scl=Pin(4), sda=Pin(5), freq=100000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello World', 0, 0, 1)
display.show()


