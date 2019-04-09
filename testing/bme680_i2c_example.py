import time
import board
from busio import I2C
import adafruit_bme680

# To use 2nd i2c bus at GPIO pin 27(SDA_1)/28(SCL_1) on Jetson Nano:
# - connect i2c sensor/oled i2c_sda  -->  jetson nano pin#27(sda_1)
# - connect i2c sesnor/oled i2c_scl  -->  jetson nano pin#28(scl_1)
# - connect i2c sensor/oled vcc(3v3) -->  jetson nano pin#17(3v3) or pin#2/4 if the sensor/oled board is 5v/3.3v compatible
# - connect i2c sesnor/oled gnd      -->  jetson nano pin#14(gnd) or any available gnd pins on board

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL_1, board.SDA_1)

# Use busio.i2c.scan() function to confirm the sensor board's i2c address before setting the address parameter
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=0x76, debug=false)

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude)

    time.sleep(1)
