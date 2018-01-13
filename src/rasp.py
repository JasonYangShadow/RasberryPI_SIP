import RPi.GPIO as GPIO
from sqlite import Sqlite
from matplot import RealPlot
from datetime import datetime
import time
import threading

IN = [18,23]

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
            GPIO.add_event_detect(i, GPIO.RISING,callback = self.__callback, bouncetime = 200)


def worker(IN, realplot):
    while True:
        for i in IN:
            input_state = GPIO.input(i)
            if input_state == False:
                realplot.add(i,datetime.now(),1)
        time.sleep(0.1)


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


class Buzzer:
    def __init__(self, OUT):
        self.__out = OUT 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__out,GPIO.OUT)
        self.__pitch = 200
        self.__duration = 0.2
        self.__period = 1.0/self.__pitch
        self.__delay = self.__period / 2
        self.__cycles = int(self.__duration * self.__pitch)

    def play(self):
        for loop in range(1,1000):
            for i in range(self.__cycles):
                GPIO.output(self.__out, True)
                time.sleep(self.__delay)
                GPIO.output(self.__out, False)
                time.sleep(self.__delay)
