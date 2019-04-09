import time
import board
from busio import I2C
import adafruit_bme680

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