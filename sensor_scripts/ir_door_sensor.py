import time
import RPi.GPIO as gpio

# Configure RPi.GPIO library to use the Broadcom chip.
gpio.setmode(gpio.BCM)

# Define door sensor pins.
door_sensor_drive_pin = 23 # PWM
door_sensor_receive_pin = 24

# Setup door sensor pins.
gpio.setup(door_sensor_drive_pin, gpio.OUT)
gpio.setup(door_sensor_receive_pin, gpio.IN)

# Setup PWM settings.
pwm = gpio.PWM(door_sensor_drive_pin, 5) # 38kHz

# Run polling loop.
pwm.start(50) # start with 50% duty cyle
try:
    while True:
        # Set default status.
        message = 'No Event'

        # Check if status needs to be updated.
        if gpio.input(door_sensor_receive_pin):
            message = 'Threshold Event'

        # Print out status.
        print(message)

        # Sleep poll interval.
        time.sleep(0.1)
except KeyboardInterrupt:
    print('Stopped')

pwm.stop()
gpio.cleanup()
