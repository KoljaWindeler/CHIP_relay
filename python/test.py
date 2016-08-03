import CHIP_IO.GPIO as GPIO
import time

GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P2", GPIO.OUT)
GPIO.setup("XIO-P4", GPIO.OUT)
GPIO.setup("XIO-P6", GPIO.OUT)

GPIO.output("XIO-P0", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P2", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P4", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P6", GPIO.HIGH)

time.sleep(10)

GPIO.output("XIO-P0", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P2", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P4", GPIO.HIGH)
time.sleep(1)
GPIO.output("XIO-P6", GPIO.HIGH)

