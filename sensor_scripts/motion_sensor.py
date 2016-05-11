import time
import RPi.GPIO as gpio

# Configure RPi.GPIO library to use the Broadcom chip.
gpio.setmode(gpio.BCM)

# Define motion sensor data pin.
motion_sensor_pin = 18

# Setup data pin.
gpio.setup(motion_sensor_pin, gpio.IN)

# Run polling loop.
try:
   while True:
      # Set default status.
      message = 'Unoccupied'

      # Check if status needs to be updated.
      if gpio.input(motion_sensor_pin):
         message = 'Occupied'

      # Print out status.
      print(message)

      # Sleep for poll interval.
      time.sleep(1.0)
except KeyboardInterrupt:
   pass

gpio.cleanup()
