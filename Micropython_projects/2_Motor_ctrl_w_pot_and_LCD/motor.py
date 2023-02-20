# Motor with LCD

import machine
import utime
from pico_i2c_lcd import I2cLcd

pwmPIN=16
cwPin=14 
acwPin=15

mtr_AI1 = machine.Pin(14,machine.Pin.OUT)
mtr_AI2 = machine.Pin(15,machine.Pin.OUT)
mtr_PWM  = machine.PWM(machine.Pin(16))

mtr_PWM.freq(50)

i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


while True:
    
    speed = 0
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(5)
    lcd.clear()
    
    
    # Direction 1
    mtr_AI1.value(0)
    mtr_AI2.value(1)
    
    speed = 100
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(5)
    lcd.clear()
    
    speed = 50
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(5)
    lcd.clear()
    
    
    speed = 0
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(2)
    lcd.clear()
    
    
    
    # Direction 2
    mtr_AI1.value(1)
    mtr_AI2.value(0)
    
    speed = 100
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(5)
    lcd.clear()
    
    speed = 50
    mtr_PWM.duty_u16(int(speed/100*65536))
    lcd.putstr("Motor Speed:"+str(int(speed)))
    utime.sleep(5)
    lcd.clear()
    

    