import ujson
import time

def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  data = request.find('/?data')
  
  if led_on == 6:
    Y1.on()
    print('LED ON')
    Y2.on()
    response = 'on'
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
  if led_off == 6:
    Y1.on()
    print('LED OFF')
    Y2.off()
    response = 'off'
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
  if data != -1:
    display.fill(0)
    Y1.on()
    d.measure()
    humidity = d.humidity()
    temp = d.temperature()
    display.text("Temperature:{}".format(temp), 0, 0, 1)
    display.text("Humidity:{}".format(humidity), 0, 20, 1)
    display.show()
    time.sleep(1)
    
    #response = "temp={} humidity={}".format(temp, humidity)
    #strTemp = "{2:2f}".format(temp)
    #strHumidity = "{2:2f}".format(humidity)
    response = ujson.dumps({'temperature': temp, 'humidity': humidity})
    print( response )
    
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: application/json\n')
    

  conn.send('Connection: close\n\n')
  
  conn.sendall(response)
  conn.close()
  Y1.off()



    
