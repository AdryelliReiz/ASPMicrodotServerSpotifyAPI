from machine import Pin, I2C
import time
import ssd1306 # https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py

def saySomething (text):
    i2c=I2C(sda=Pin(5), scl=Pin(4))
    display=ssd1306.SSD1306_I2C(128,64,i2c)
    for x in range(2):
        display.fill(0)
        display.text(text,10,10,1)
        display.show()
        time.sleep(1)
    display.fill(0)

def saying (text):
    i2c=I2C(sda=Pin(5), scl=Pin(4))
    display=ssd1306.SSD1306_I2C(128,64,i2c)
    
    display.fill(0)
    display.text(text,10,10,1)
    display.show()