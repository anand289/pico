# for this code to work, no other ADC terminal should be connected to anything. 

import machine
import utime

sensor_temp = machine.ADC(4)
conversion_factor = (3.3)/(65535)

from pico_i2c_lcd import I2cLcd

i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

reading = sensor_temp.read_u16()*conversion_factor
t_prev = 27 - ((reading - 0.706)/(0.001721))
t_prev = round(t_prev,2)

while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temperature = 27 - ((reading - 0.706)/(0.001721))
    
    temperature = round(temperature,2)
    t = temperature
    
    if (t != t_prev):
        lcd.clear()
        lcd.putstr("Temp (C): "+str(t))
        t_prev = t
        print("Temperature:", t, "C")
    
    utime.sleep(1)
    
    