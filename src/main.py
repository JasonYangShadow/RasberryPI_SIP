#!/bin/python3
from matplot import RealPlot
from sqlite import Sqlite
from rasp import Buzzer, MCP 
import time

if __name__ == '__main__':
    realplot = RealPlot() 
    #buzz = Buzzer(26)
    #buzz.play()
    mcp = MCP(18,23,24,25)
    mcp.run(3.3,realplot)
    realplot.show()
