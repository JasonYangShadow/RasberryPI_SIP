#!/bin/python3
from matplot import RealPlot
from sqlite import Sqlite
from rasp import Rasp

if __name__ == '__main__':
    realplot = RealPlot() 
    rp = Rasp(realplot)
    rp.run()
    realplot.show()
