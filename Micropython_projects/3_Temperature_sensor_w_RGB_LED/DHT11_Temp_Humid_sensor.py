'''
temperature and humidity sensor using DHT11.
led will turn red when temp near max_temp,
and blue when temp. near min_temp

same can be selected for humidity
blue -> near max_humd
red -> near min_humd
'''


import machine
import utime
import dht
from pico_i2c_lcd import I2cLcd


temp_PWM_blue  = machine.PWM(machine.Pin(20))
temp_PWM_green  = machine.PWM(machine.Pin(18))
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


max_temp = 35 # when led should only show red
min_temp = 10 # when led should only show blue

max_humd = 60
min_humd = 20

# intercept of a line passing through (x1,y1) (x2,y2)  = (y1*x2 - y2*x1)/(x2-x1)
blue_intercept = (max_temp*65536-min_temp*0)/(max_temp - min_temp)
red_intercept = (0*max_temp-65536*min_temp )/(max_temp - min_temp)

# for humidity
red_intercept_humd = (max_humd*65536-min_humd*0)/(max_humd - min_humd)
blue_intercept_humd = (0*max_humd-65536*min_humd)/(max_humd - min_humd)

def set_temperature_color(temp):
    temp_PWM_red.duty_u16(int((65536-0)*temp/(max_temp-min_temp) + red_intercept)) # line passing through two points (max_temp,65536) and (min_temp,0)
    temp_PWM_green.duty_u16(int(0)) #off                      
    temp_PWM_blue.duty_u16(int((0-65536)*temp/(max_temp-min_temp) + blue_intercept)) # line passing through two points (max_temp,0) and (min_temp,65536)
    
def set_humidity_color(humd):
    temp_PWM_blue.duty_u16(int((65536-0)*humd/(max_humd-min_humd) + blue_intercept_humd)) # line passing through two points (max_temp,65536) and (min_temp,0)
    temp_PWM_green.duty_u16(int(0)) #off                      
    temp_PWM_red.duty_u16(int((0-65536)*humd/(max_humd-min_humd) + red_intercept_humd)) # line passing through two points (max_temp,0) and (min_temp,65536)
    

#set_temperature_color(d.temperature())
set_humidity_color(d.humidity())   
    
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
        
        
       # set_temperature_color(d.temperature())
        set_humidity_color(d.humidity())


