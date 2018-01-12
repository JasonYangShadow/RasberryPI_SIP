import RPi.GPIO as GPIO
from sqlite import Sqlite
from matplot import RealPlot
from datetime import datetime
import time

IN = [18]

class Rasp:
    
    def __init__(self,realplot):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.__sqlite = Sqlite() 
        self.__sqlite.create_table('hist_data')
        self.__realplot = realplot

    def __callback_realtime(self,chanel):
        self.__realplot.add(chanel,datetime.now(),1)

    def __callback_sqlite(self,chanel):
        self.__sqlite.insert_table(chanel,'hist_data')

    def run(self):
        for i in IN:
            GPIO.add_event_detect(i, GPIO.RISING)
            GPIO.add_event_callback(i, GPIO.RISING, call_back = self.__callback_realtime, bouncetime = 100)
            GPIO.add_event_callback(i, GPIO.RISING, call_back = self.__callback_sqlite, bouncetime = 100)


