'''
temperature and humidity sensor using DHT11.
led will turn red when temp near max_temp,
and blue when temp. near min_temp
'''


import machine
import utime
import dht
from pico_i2c_lcd import I2cLcd


temp_PWM_blue  = machine.PWM(machine.Pin(21))
temp_PWM_green  = machine.PWM(machine.Pin(20))
temp_PWM_red  = machine.PWM(machine.Pin(19))
temp_PWM_blue.freq(50)
temp_PWM_green.freq(50)
temp_PWM_red.freq(50)



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


max_temp = 27 # when led should only show red
min_temp = 12 # when led should only show blue

# intercept of a line passing through (x1,y1) (x2,y2)  = (y1*x2 - y2*x1)/(x2-x1)
red_intercept = (max_temp*65536-min_temp*0)/(max_temp - min_temp)
blue_intercept = (0*max_temp-65536*min_temp )/(max_temp - min_temp)

def set_temperature_color(temp):
    temp_PWM_red.duty_u16(int((0-65536)*temp/(max_temp-min_temp) + red_intercept)) # line passing through two points (10,65536) and (30,0)
    temp_PWM_green.duty_u16(int(65536)) #off                      
    temp_PWM_blue.duty_u16(int((65536-0)*temp/(max_temp-min_temp) + blue_intercept)) # line passing through two points (10,0) and (30,65536)

set_temperature_color(d.temperature())
    
while True:
    
    d.measure()
    t = d.temperature()
    h = d.humidity()

    
    if (t != t_prev) or (h !=h_prev):
        lcd.clear()
        lcd.putstr("Temp (C): "+str(t))
        lcd.putstr("\nHmd (%): "+str(h))
        t_prev = t
        h_prev = h
        
        # print temperature and humidity when changed
        print("Temperature:", d.temperature(), "C")
        print("Humidity:", d.humidity(), "%")
        
        
        set_temperature_color(d.temperature())

