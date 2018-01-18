import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sqlite import Sqlite
from datetime import datetime

maxsize = 50

class RealPlot:
    
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__data = {} 

    def add(self,chanel,x,y):
        if chanel in self.__data:
            if len(self.__data[chanel]['x']) >= maxsize:
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
        ani = animation.FuncAnimation(self.__fig, self.__animate, interval = 1000)
        plt.show()


class HistPlot:
   
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__sqlite = Sqlite()

    def show(self):
        rows = self.__sqlite.query_bytime('hist_data')

