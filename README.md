# bme680-raspi

### Dependencies
pip3, adafruit-circuitpython-bme680, board, busio

### Usage
1. Install dependencies using pip3 and if wanted a venv. 

2. Run `python3 main.py`

### Supported Platforms
Tested to work on a Raspberry Pi 3B v1.2. Looks for a BME680 at I2C address `0x77`. That is the default address for the adafruit model. Uses the default SCL and SDA pins on the raspi.