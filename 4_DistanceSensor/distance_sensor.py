import machine
import utime

en = machine.Pin(27,machine.Pin.OUT)
out = machine.Pin(26,machine.Pin.IN)

while True:

  #  lcd.putstr("Out Vol:"+str(out.read_u16()))
    en.value(1)
    if out.value() == 0:
        print("Sensed")
    utime.sleep(0.2)
    en.value(0)
  #  lcd.clear()
    