import RPi.GPIO as GPIO
from sqlite import Sqlite
from matplot import RealPlot
from datetime import datetime
import time
import threading

IN = [18]

class Rasp:
    
    def __init__(self,realplot):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #self.__sqlite.create_table('hist_data')
        self.__realplot = realplot

    def __callback(self,chanel):
        self.__realplot.add(chanel,datetime.now(),1)
        #self.__sqlite.insert_table(chanel,'hist_data')

    def run(self):
        for i in IN:
            GPIO.add_event_detect(i, GPIO.RISING,callback = self.__callback, bouncetime = 2000)


def worker(IN, realplot):
    while True:
        for i in IN:
            input_state = GPIO.input(i)
            if input_state == False:
                realplot.add(i,datetime.now(),1)
        time.sleep(0.2)


class RaspIter:

    def __init__(self,realplot):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        self.__sqlite = Sqlite() 
        #self.__sqlite.create_table('hist_data')
        self.__realplot = realplot

    def run(self):
        t = threading.Thread(target = worker,args = (IN, self.__realplot))
        t.start()

