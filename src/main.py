#!/bin/python3
from matplot import RealPlot
from sqlite import Sqlite
from rasp import RaspIter 

if __name__ == '__main__':
    realplot = RealPlot() 
    rp = RaspIter(realplot)
    rp.run()
    realplot.show()
