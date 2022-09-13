# running on Adafruit QT Py ESP32-S2 WiFi Dev Board with STEMMA QT
# I use this instead of a rpi because pis are hard to find these days and this sensor gets the job done for less than half the price
# the QT Py blinks certain colors if it's successfully posting or retrying so I have a visual indicator in my daily life
# the code is almost the same on a pi, except you can use the actual python libraries instead of the micropython versions

import ssl
import wifi
import socketpool
import neopixel
import board
import busio
import time
import adafruit_veml7700 #light sensor library
import adafruit_ahtx0 #temp and humidity sensor
from adafruit_seesaw.seesaw import Seesaw #soil sensor library

import adafruit_requests as requests

try:
	from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

BASE_URL = "https://dash-customer-success.plotly.host/plant-data-receptor"
api_endpoint = "/readings"

i2c_bus = board.I2C()
#i2c = busio.I2C(board.SCL, board.SDA)
veml7700 = adafruit_veml7700.VEML7700(i2c_bus)

soil_sensor_1 = Seesaw(i2c_bus, addr=0x36)
soil_sensor_2 = Seesaw(i2c_bus, addr=0x37)
soil_sensor_3 = Seesaw(i2c_bus, addr=0x39)
lux_sensor = adafruit_veml7700.VEML7700(i2c_bus)
temp_sensor = adafruit_ahtx0.AHTx0(i2c_bus)


def readings_loop():
    soil_1_reading = soil_sensor_1.moisture_read()
    https.post(BASE_URL+api_endpoint+"/"+"2001"+"/"+str(soil_1_reading))

    soil_2_reading = soil_sensor_2.moisture_read()
    https.post(BASE_URL+api_endpoint+"/"+"2002"+"/"+str(soil_2_reading))

    soil_3_reading = soil_sensor_3.moisture_read()
    https.post(BASE_URL+api_endpoint+"/"+"2004"+"/"+str(soil_3_reading))

    ambient_reading = veml7700.light
    https.post(BASE_URL+api_endpoint+"/"+"2005"+"/"+str(ambient_reading))

    lux_reading = veml7700.lux
    https.post(BASE_URL+api_endpoint+"/"+"2000"+"/"+str(lux_reading))

    temp_reading = temp_sensor.temperature
    https.post(BASE_URL + api_endpoint + "/" + "2003" + "/" + str(temp_reading))

    humidity_reading = temp_sensor.relative_humidity
    https.post(BASE_URL+api_endpoint+"/"+"2006"+"/"+str(humidity_reading))
    return

while True:
    try:
        readings_loop()
        pixels.fill((125, 50, 168))
        time.sleep(0.5)
        pixels.fill((50, 160, 168))
        time.sleep(0.5)
        pixels.fill((50, 168, 50))
        time.sleep(60000)
    except:
        pixels.fill((235, 87, 193))
        time.sleep(60000)

    print("readings posted")

