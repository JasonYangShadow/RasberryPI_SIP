import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sqlite import Sqlite

class MatPlot:

    def __init__(self,title,label_x,label_y):
        self.__fig = plt.figure()
        plt.title(title)
        plt.xlabel(label_x)
        plt.ylabel(label_y)
        self.__x = []
        self.__y = []
        self.__sqlite = Sqlite()

    def gen_data(self,table = 'real_data'):
        rows = self.__sqlite.query_delete(table)
        for r in rows:
            self.__x.append(r[1])
            self.__y.append(1)

    def animate(self):
        return plt.plot(self.__x,self.__y, color ='g')

    def show(self):
        anim = animation.FuncAnimation(self.__fig,self.animate,frames = self.gen_data,interval = 1000)
        plt.show()


if __name__ == '__main__':
    plot = MatPlot('real_time','time(s)','count')
    plot.show()
