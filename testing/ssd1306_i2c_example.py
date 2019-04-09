# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



'''
usage of jetson nano's gpio
qing.wei@live.com, 2019.04.09 
'''

# jetson nano board definition: https://github.com/adafruit/Adafruit_Blinka/blob/master/src/adafruit_blinka/board/jetson_nano.py
# note: the gpio pin number used in adafruit blinka python library is to follow the Raspberry Pi GPIO naming system not the pin sequence on board 
# - i2c pins: (can not be used as gpio)
#   SDA = pin.SDA_1 (pin #3)
#   SCL = pin.SCL_1 (pin #5)
#   SDA_1 = pin.SDA (pin #27)
#   SCL_1 = pin.SCL (pin #28)

# - uart pins: (not defined yet as of 2019-04-09. can not be used as gpio)
#   TXD0 = pin.GPIO14 (pin #8)
#   RXD0 = pin.GPIO15 (pin #10)

# - spi/i2s: nil

# - gpio pins:
#   D4 = pin.BB00 (pin #7)
#   D5 = pin.S05 (pin #29)
#   D6 = pin.Z00 (pin #31)
#   D7 = pin.C04 (pin #26)
#   D8 = pin.C03 (pin #24)
#   D9 = pin.C01 (pin #21)
#   D10 = pin.C00 (pin #19)
#   D11 = pin.C02 (pin #23)
#   D12 = pin.V00 (pin #32)
#   D13 = pin.E06 (pin #33)
#   D16 = pin.G03 (pin #36)
#   D17 = pin.G02 (pin #11)
#   D18 = pin.J07 (pin #12)
#   D19 = pin.J04 (pin #35)
#   D20 = pin.J05 (pin #38)
#   D21 = pin.J06 (pin #40)
#   D22 = pin.Y02 (pin #15)
#   D23 = pin.DD00 (pin #16)
#   D24 = pin.B07 (pin #18)
#   D25 = pin.B05 (pin #22)
#   D26 = pin.B04 (pin #37)
#   D27 = pin.B06 (pin #13)

# To use 2nd i2c bus at GPIO pin 27(SDA_1)/28(SCL_1) on Jetson Nano:
# - connect i2c sensor/oled i2c_sda  -->  jetson nano pin#27(sda_1)
# - connect i2c sesnor/oled i2c_scl  -->  jetson nano pin#28(scl_1)
# - connect i2c sensor/oled vcc(3v3) -->  jetson nano pin#17(3v3) or pin#2/4 if the sensor/oled board is 5v/3.3v compatible
# - connect i2c sesnor/oled gnd      -->  jetson nano pin#14(gnd) or any available gnd pins on board

'''
ref: ~/jetbot/.local/lib/python3.6/site-packages/Jetson/GPIO/gpio_pin_data.py:
JETSON_NANO_PIN_DEFS = [
#   (tegra210_pin,    <->          , brd_pin#, rpi_pin_name, <->, <->)     
    (216, "/sys/devices/6000d000.gpio", 7, 4, 'AUDIO_MCLK', 'AUD_MCLK'),
    (50, "/sys/devices/6000d000.gpio", 11, 17, 'UART2_RTS', 'UART2_RTS'),
    (79, "/sys/devices/6000d000.gpio", 12, 18, 'DAP4_SCLK', 'DAP4_SCLK'),
    (14, "/sys/devices/6000d000.gpio", 13, 27, 'SPI2_SCK', 'SPI2_SCK'),
    (194, "/sys/devices/6000d000.gpio", 15, 22, 'LCD_TE', 'LCD_TE'),
    (232, "/sys/devices/6000d000.gpio", 16, 23, 'SPI2_CS1', 'SPI2_CS1'),
    (15, "/sys/devices/6000d000.gpio", 18, 24, 'SPI2_CS0', 'SPI2_CS0'),
    (16, "/sys/devices/6000d000.gpio", 19, 10, 'SPI1_MOSI', 'SPI1_MOSI'),
    (17, "/sys/devices/6000d000.gpio", 21, 9, 'SPI1_MISO', 'SPI1_MISO'),
    (13, "/sys/devices/6000d000.gpio", 22, 25, 'SPI2_MISO', 'SPI2_MISO'),
    (18, "/sys/devices/6000d000.gpio", 23, 11, 'SPI1_SCK', 'SPI1_SCK'),
    (19, "/sys/devices/6000d000.gpio", 24, 8, 'SPI1_CS0', 'SPI1_CS0'),
    (20, "/sys/devices/6000d000.gpio", 26, 7, 'SPI1_CS1', 'SPI1_CS1'),
    (149, "/sys/devices/6000d000.gpio", 29, 5, 'CAM_AF_EN', 'CAM_AF_EN'),
    (200, "/sys/devices/6000d000.gpio", 31, 6, 'GPIO_PZ0', 'GPIO_PZ0'),
    (168, "/sys/devices/6000d000.gpio", 32, 12, 'LCD_BL_PWM', 'LCD_BL_PW'),
    (38, "/sys/devices/6000d000.gpio", 33, 13, 'GPIO_PE6', 'GPIO_PE6'),
    (76, "/sys/devices/6000d000.gpio", 35, 19, 'DAP4_FS', 'DAP4_FS'),
    (51, "/sys/devices/6000d000.gpio", 36, 16, 'UART2_CTS', 'UART2_CTS'),
    (12, "/sys/devices/6000d000.gpio", 37, 26, 'SPI2_MOSI', 'SPI2_MOSI'),
    (77, "/sys/devices/6000d000.gpio", 38, 20, 'DAP4_DIN', 'DAP4_DIN'),
    (78, "/sys/devices/6000d000.gpio", 40, 21, 'DAP4_DOUT', 'DAP4_DOUT')
]

'''


import time

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from jetbot.utils.utils import get_ip_address

import subprocess

# 128x64 display with hardware I2C:
# set i2c_bus=0 to use the 2nd i2c bus. i2c_bus=1 to use the first i2c bus.  
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_bus=0, gpio=1) # setting gpio to 1 is hack to avoid platform detection

# Initialize library.
# 0x3c as i2c address of ssd1306. can use busio.i2c.scan() to check the actual i2c address of different boards
disp.begin(0x3c)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()


while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True )

    # Write two lines of text.

    draw.text((x, top),       "eth0: " + str(get_ip_address('eth0')),  font=font, fill=255)
    draw.text((x, top+8),     "wlan0: " + str(get_ip_address('wlan0')), font=font, fill=255)
    draw.text((x, top+16),    str(MemUsage.decode('utf-8')),  font=font, fill=255)
    draw.text((x, top+25),    str(Disk.decode('utf-8')),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(1)
