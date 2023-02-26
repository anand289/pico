import machine
import utime

board_led = machine.Pin(25,machine.Pin.OUT)



while True:
    board_led.value(1)
    utime.sleep(1)
    board_led.value(0)
    utime.sleep(1)