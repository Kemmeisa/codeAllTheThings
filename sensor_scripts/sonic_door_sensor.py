import time
import RPi.GPIO as gpio

# Configure RPi.GPIO library to use the Broadcom chip.
gpio.setmode(gpio.BCM)

# Define door sensor pin.
door_sensor_pin = 23

# Define timeout.
timeout = 0.020

# Run loop.
try:
    while True:
        # Setup door sensor pin for output and turned off.
        gpio.setup(door_sensor_pin, gpio.OUT)
        gpio.output(door_sensor_pin, 0)

        # Delay time for setup to finish.
        time.sleep(0.000002)

        # Send signal.
        gpio.output(door_sensor_pin, 1)

        # Duration for sending signal.
        time.sleep(0.5)

        # Setup door sensor pin for input and turned off.
        gpio.output(door_sensor_pin, 0)
        gpio.setup(door_sensor_pin, gpio.IN)

        # Read distance.
        success = True
        watchTime = time.time()
        while success and 0 == gpio.input(door_sensor_pin):
            startTime = time.time()
            if (timeout < startTime - watchTime):
                success = False

        if success:
            watchTime = time.time()
            while success and gpio.input(door_sensor_pin) == 1:
                endTime = time.time()
                if (timeout < endTime - watchTime):
                    success = False

        if success:
            duration = endTime - startTime
            distance = duration * 34000 / 2
            print ("Distance: %0.2f" % distance)
except KeyboardInterrupt:
    pass

# Cleanup GPIO.
gpio.cleanup()
