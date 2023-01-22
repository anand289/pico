import machine
import utime

pwmPIN=16
cwPin=14 
acwPin=15

mtr_AI1 = machine.Pin(14,machine.Pin.OUT)
mtr_AI2 = machine.Pin(15,machine.Pin.OUT)
mtr_PWM  = machine.PWM(machine.Pin(16))

mtr_PWM.freq(50)



while True:
    
    speed = 0
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(5)
    
    # Direction 1
    mtr_AI1.value(0)
    mtr_AI2.value(1)
    
    speed = 100
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(5)
    
    speed = 50
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(5)
    
    
    speed = 0
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(2)
    
    
    
    # Direction 2
    mtr_AI1.value(1)
    mtr_AI2.value(0)
    
    speed = 100
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(5)
    
    speed = 50
    mtr_PWM.duty_u16(int(speed/100*65536))
    utime.sleep(5)
    

    