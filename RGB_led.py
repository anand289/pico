import machine
import utime
from pico_i2c_lcd import I2cLcd


led_red = machine.Pin(13,machine.Pin.OUT)
led_green = machine.Pin(12,machine.Pin.OUT)
led_blue = machine.Pin(11,machine.Pin.OUT)

rgb_led_ref = machine.Pin(18,machine.Pin.OUT)
rgb_led_ref.value(1)

potentiometer = machine.ADC(28)


i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)



while True:
    
    
    lcd.putstr("Red \n")
    lcd.putstr("Pot Vol:"+str(potentiometer.read_u16())) 
    led_red.value(0)
    led_green.value(1)
    led_blue.value(1)
    utime.sleep(1)
    lcd.clear()
    
    lcd.putstr("Green \n")
    lcd.putstr("Pot Vol:"+str(potentiometer.read_u16())) 
    led_red.value(1)
    led_green.value(0)
    led_blue.value(1)
    utime.sleep(1)
    lcd.clear()
    
    lcd.putstr("Blue \n")

    lcd.putstr("Pot Vol:"+str(potentiometer.read_u16())) 
    led_red.value(1)
    led_green.value(1)
    led_blue.value(0)
    utime.sleep(1)
    lcd.clear()
    
    #print(potentiometer.read_u16())
    