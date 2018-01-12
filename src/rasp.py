#!/bin/python3
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("cound not import GPIO. please use pip install to install the package")
import time
from sqlite import Sqlite

IN = []
OUT = []

class Rasp:
    
    def __init__(self,sqldb):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(OUT, GIIO.OUT, pull_up_down = GPIO.PUD_DOWN)
        self.__sqlite = Sqlite() 

    def __callback_realtime(self,chanel):
        self.__sqlite.insert_table(chanel, 'real_data')

    def __callback_sqlite(self,chanel):
        self.__sqlite.insert_table(chanel,'hist_data')

    def run(self):
        for i in IN:
            GPIO.add_event_detect(i, GPIO.RISING)
            GPIO.add_event_callback(i, GPIO.RISING, call_back = self.__callback_realtime, bouncetime = 100)
            GPIO.add_event_callback(i, GPIO.RISING, call_back = self.__callback_sqlite, bouncetime = 100)


