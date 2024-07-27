from gpiozero import DistanceSensor
import time
import BlynkLib
from BlynkTimer import BlynkTimer

# Initialize Blynk
blynk = BlynkLib.Blynk("BrLkWMYQFxL1Snk1gGAy1WVHp2M6XXYn")

# Create BlynkTimer Instance
timer = BlynkTimer()

# Initialize the DistanceSensor
sensor = DistanceSensor(echo=22, trigger=27)

# Function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Hi, You have Connected to New Blynk2.0")
    print(".......................................................")
    time.sleep(2)

# Function to collect data from the distance sensor & send it to the server
def send_distance_data():
    distance = sensor.distance * 100  # Convert to centimeters
    print(f"Distance = {distance:.1f} cm")
    blynk.virtual_write(0, distance)  # Sending distance data to virtual pin V2
    print("Distance sent to New Blynk Server!")

timer.set_interval(5, send_distance_data)

while True:
    blynk.run()
    timer.run()
    time.sleep(1)
