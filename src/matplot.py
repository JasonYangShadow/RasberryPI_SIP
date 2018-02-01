import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sqlite import Sqlite
from datetime import datetime
import statistics

MAXSIZE = 300 
INTERVAL = 200
ALERT_TIME = 5

class RealPlot:
    
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__data = {} 

    def add(self,chanel,x,y):
        if chanel in self.__data:
            if len(self.__data[chanel]['x']) >= MAXSIZE:
                self.__data[chanel]['x'].pop(0)
                self.__data[chanel]['y'].pop(0)
            self.__data[chanel]['x'].append(x)
            self.__data[chanel]['y'].append(y)
        else:
            self.__data[chanel] = {}
            self.__data[chanel]['x']=[]
            self.__data[chanel]['y']=[]

    def __animate(self,i):
        self.__ax.clear()
        plt.title('realtime signal voltage')
        plt.xlabel('time(s)')
        plt.ylabel('voltage(V)')
        legend = []
        for chanel in self.__data.keys():
            #self.add(chanel,datetime.now(),0)
            self.__ax.plot(self.__data[chanel]['x'],self.__data[chanel]['y'])
            legend.append(['chanel:'+str(chanel)])
        plt.legend(legend)


    def show(self):
        ani = animation.FuncAnimation(self.__fig, self.__animate, interval = INTERVAL)
        plt.show()

class TuplePlot: 
    
    def __init__(self,buzz):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__data = {} 
        self.__count = int(ALERT_TIME*1000/INTERVAL)
        self.__ccount = {} 
        self.__buzz = buzz 

    def add(self,chanel,tuple):
        if chanel in self.__data:
            if len(self.__data[chanel]) >= MAXSIZE:
                self.__data[chanel].pop(0)
            self.__data[chanel].append(tuple)
        else:
            self.__data[chanel] = []
            self.__ccount[chanel] = 0 
    
    def __animate(self,i):
        self.__ax.clear()
        plt.title('realtime signal voltage')
        plt.xlabel('time(s)')
        plt.ylabel('voltage(V)')
        legend = []
        for chanel in self.__data.keys():
            x = [item[0] for item in self.__data[chanel]]
            y = [item[1] for item in self.__data[chanel]]
            print("stdev=>"+str(statistics.stdev(y))+" count=>"+str(self.__ccount[chanel]))
            if statistics.stdev(y) < 0.2:
                self.__ccount[chanel] += 1
            else:
                self.__ccount[chanel] = 0
            if self.__ccount[chanel] >= self.__count:
                plt.title("ALLERT!! NOT ENOUGH SIGNAL FLUCTUATION ON CHANEL: "+str(chanel),fontsize = 12, color = 'red')
                self.__buzz.play()
            self.__ax.plot(x,y)
            legend.append(['chanel:'+str(chanel)])
        plt.legend(legend)

    def show(self):
        ani = animation.FuncAnimation(self.__fig, self.__animate, interval = INTERVAL)
        plt.show()


class HistPlot:
   
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__sqlite = Sqlite()

    def show(self):
        rows = self.__sqlite.query_bytime('hist_data')

