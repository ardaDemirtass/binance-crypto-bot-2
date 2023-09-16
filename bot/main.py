from binanceapi.binanceapi import BinanceAPI
from graph.candle import Graph
from model.lrmodel import LinearModel
import matplotlib.pyplot as plt
from model.loadmodel import LoadModel
from model.basemodel import BaseModel
from bot import Bot
import time

print('to display commands, type **help')
bncapi = BinanceAPI('GMT')
kli = bncapi.GetHistoricalKlines('ETHBUSD')
x = kli.iloc[364,0:4].values.reshape(1,-1)
while True:
    command = input('->')
    commandSplit = command.split('-')
    if commandSplit[0] == "**runbot":
        symbols = input("write symbols to run : ")
        symbolsSplit = symbols.split('-')
        bot = Bot(symbolsSplit)
        bot.RunBot()
    if commandSplit[0] == "**drawgraph":
        try:
            klines = bncapi.GetHistoricalKlines(commandSplit[1])
            gr = Graph(klines)
            gr.Draw()
        except:
            print('unknown symbol')
            pass
    if commandSplit[0] == "**learn":
        symbol = commandSplit[1]
        klines = bncapi.GetHistoricalKlines(symbol=symbol)
        x=klines.iloc[:,0:4]
        y=klines.iloc[:,4:5]
        try:
            lr = LinearModel(symbol=symbol, input=x, output=y)
            lr.CreateModel()
            lr.SaveModel()
        except:
            print("error - cannot save model")
    if commandSplit[0] == "**exit":
        break
    if commandSplit[0] == "**data":
        symbol = commandSplit[1]
        klines = bncapi.GetHistoricalKlines(symbol=symbol)
        print(klines)
"""
bncapi = BinanceAPI('GMT')
kli = bncapi.GetHistoricalKlines('ETHBUSD')
print(kli.iloc[0:364,:])
input=kli.iloc[0:364,0:4]
output=kli.iloc[0:364,4:5]
lr = LinearModel(symbol='ETHBUSD', input=input, output=output)
lr.CreateModel()
lr.SaveModel()
lm = LoadModel('ETHBUSD', 'LR')
print(lm.Model.Predict(kli.iloc[364,0:4].values.reshape(1,-1)))
gr = Graph(kli)
gr.Draw()

print(lr.Predict(kli.iloc[364,0:4].values.reshape(1,-1)))

plt.plot(kli.iloc[0:364,0:1], kli.iloc[0:364,4:5])
plt.plot(kli.iloc[0:364, 0:1], lr.Predict(kli.iloc[0:364,0:4].values))
plt.show()
"""