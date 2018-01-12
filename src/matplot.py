import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sqlite import Sqlite

class RealPlot:
    
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.data = {} 
        self.lines = []

    def add(self,chanel,x,y):
        if chanel in self.data:
            self.data[chanel]['x'].append(x)
            self.data[chanel]['y'].append(y)
        else:
            self.data[chanel] = {}
            self.data[chanel]['x']=[]
            self.data[chanel]['y']=[]

    def __animate(self,i):
        self.__ax.clear()
        self.lines.clear()
        for key in self.data.keys():
            line, = self.__ax.plot(self.data[key]['x'],self.data[key]['y'])
            self.lines.append(line)
            plt.legend(handles = [line])

    def show(self):
        plt.title('realtime signal')
        plt.xlabel('time(s)')
        plt.ylabel('bool signal')
        plt.ylim(0,1)
        ani = animation.FuncAnimation(self.__fig, self.__animate, interval = 1000)
        plt.show()


class HistPlot:
   
    def __init__(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__sqlite = Sqlite()

    def show(self):
        rows = self.__sqlite.query_bytime('hist_data')
