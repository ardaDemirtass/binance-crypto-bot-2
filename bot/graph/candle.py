import matplotlib.pyplot as plt
import pandas as pd

class Graph:
    def __init__(self, df : pd.DataFrame):
        self.__Df = df

    def Draw(self):
        plt.figure()
        width = .4
        width2 = .05
        up = self.__Df[self.__Df.close >= self.__Df.open]
        down = self.__Df[self.__Df.close < self.__Df.open]
        col1 = 'green'
        col2 = 'red'

        plt.bar(up.index,up.close-up.open,width,bottom=up.open,color=col1)
        plt.bar(up.index,up.high-up.close,width2,bottom=up.close,color=col1)
        plt.bar(up.index,up.low-up.open,width2,bottom=up.open,color=col1)

        plt.bar(down.index,down.close-down.open,width,bottom=down.open,color=col2)
        plt.bar(down.index,down.high-down.open,width2,bottom=down.open,color=col2)
        plt.bar(down.index,down.low-down.close,width2,bottom=down.close,color=col2)

        plt.xticks(rotation=45, ha='right')
        plt.show()