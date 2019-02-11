# micropython-st7735-esp8266

### Changelog:
1. Fixed SPI to always send Bytearrays
2. Added Option to rotate Display

### Rotating
You can rotate the display by either 90, 180 or 270 degrees.
Rotating can be done:

when creating TFT Object:
```python
tft = TFT_GREEN(width, height, spi, dc, cs, rst, rotate=90)
```

or during runtime:
```python
tft.changeRotate(270)
```

### Credits
<a href="https://github.com/hosaka/">hosaka</a> who wrote the initial driver
