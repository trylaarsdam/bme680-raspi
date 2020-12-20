import time
import board
from busio import I2C
import adafruit_bme680

i2c = I2C(board.SCL, board.SDA)
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure = 1013.25 #sea level pressure in hPa

while 1:
    print("/nTemperature: %0.1f C" % bme680.temperature)
    print("Gas: %0.1f ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.relative_humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f m" % bme680.altitude)

    time.sleep(5)