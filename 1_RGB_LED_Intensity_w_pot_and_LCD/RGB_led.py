import machine
import utime
from pico_i2c_lcd import I2cLcd


led_red = machine.Pin(19,machine.Pin.OUT)
led_green = machine.Pin(20,machine.Pin.OUT)
led_blue = machine.Pin(21,machine.Pin.OUT)


potentiometer = machine.ADC(28)


i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)



while True:
    
    pot_value = int(potentiometer.read_u16()/500)
    
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
    
    # Write a function in lcdAPI that's able to display the bar on lcd. 
#   lcd.fill_rect(1,15,pot_value,25,1)
#   lcd.putstr()
#   lcd.fill_rect(1,15,pot_value,25,0)
#   utime.sleep()
    
    
    #print(potentiometer.read_u16())
