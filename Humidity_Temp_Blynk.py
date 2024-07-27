import board
import BlynkLib
from BlynkTimer import BlynkTimer
import adafruit_dht
import time

DHT_SENSOR = adafruit_dht.DHT11(board.D27)

# Initialize Blynk
blynk = BlynkLib.Blynk("f6UDsgEG_Y2in5-D-grXnNMTfSC_b-4E")

# Create BlynkTimer Instance
timer = BlynkTimer()

# Function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Hi, You have Connected to New Blynk2.0")
    print(".......................................................")
    time.sleep(2)

# Function to collect data from sensor & send it to Server
def myData():
    for _ in range(5):  # Retry up to 5 times
        try:
            humidity = DHT_SENSOR.humidity
            temperature = DHT_SENSOR.temperature
            if humidity is not None and temperature is not None:
                print(f"Temp={temperature:0.1f}C Humidity={humidity:0.1f}%")
                blynk.virtual_write(0, humidity)
                blynk.virtual_write(1, temperature)
                print("Values sent to New Blynk Server!")
                return
        except RuntimeError as error:
            print(f"Error reading DHT sensor: {error.args}")
            time.sleep(2)  # Wait before retrying

    print("Sensor failure. Check wiring.")

timer.set_interval(5, myData)

while True:
    blynk.run()
    timer.run()
