import machine
import utime
import dht
from pico_i2c_lcd import I2cLcd

# initialize DHT11 sensor on pin 26
d = dht.DHT11(machine.Pin(26))


i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

d.measure()
lcd.putstr("Temp (C): "+str(d.temperature()))
lcd.putstr("\nHmd (%): "+str(d.humidity()))

t_prev = d.temperature()
h_prev = d.humidity()

while True:
    
    # print temperature and humidity
    print("Temperature:", d.temperature(), "C")
    print("Humidity:", d.humidity(), "%")
    
    d.measure()
    t = d.temperature()
    h = d.humidity()
    
    utime.sleep(2
                )
    
    if (t != t_prev) or (h !=h_prev):
        lcd.clear()
        lcd.putstr("Temp (C): "+str(t))
        lcd.putstr("\nHmd (%): "+str(h))
        t_prev = t
        h_prev = h

