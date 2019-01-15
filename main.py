# MicroPython ST7735 TFT display driver example usage

from machine import Pin, SPI
from tft import TFT_GREEN
import font

# DC       - RS/DC data/command flag
# CS       - Chip Select, enable communication
# RST/RES  - Reset
dc  = Pin(4, Pin.OUT)
cs  = Pin(2, Pin.OUT)
rst = Pin(5, Pin.OUT)
# SPI Bus (CLK/MOSI/MISO)
# check your port docs to see which Pins you can use
spi = SPI(1, baudrate=8000000, polarity=1, phase=0)

# TFT object, this is ST7735R green tab version
tft = TFT_GREEN(128, 160, spi, dc, cs, rst)

# init TFT
tft.init()

# start using the driver

tft.clear(tft.rgbcolor(0, 0, 0)) #b, g, r
tft.text(0,0,"Test", font.terminalfont, tft.rgbcolor(255, 255, 255), 3)
tft.text(0,24,"Test", font.terminalfont, tft.rgbcolor(255, 255, 255), 3)