#!/bin/python3
from matplot import RealPlot
from sqlite import Sqlite
from rasp import Buzzer, MCP, Sound 
import time

def run_plot():
    realplot = RealPlot()
    mcp = MCP(18,23,24,25)
    mcp.run(3.3,realplot)
    realplot.show() 

def buzz():
    buzz = Buzzer(26)
    buzz.play()

def playMP3():
    sound = Sound()
    #sound.generateMP3(u'Alert!Alert!No movement detected!', 'en', False, '/tmp/en.mp3')
    #sound.generateMP3(u'注意！注意！无法检测到运动！', 'zh-cn', False, '/tmp/zh.mp3')
    #sound.generateMP3(u'注意！注意！運動は検出されませんでした', 'ja', False, '/tmp/ja.mp3')
    #time.sleep(2)
    sound.playMP3('ja.mp3')
    sound.playMP3('en.mp3')
    sound.playMP3('zh.mp3')

if __name__ == '__main__':
    playMP3()
   
