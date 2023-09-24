from binanceapi.binanceapi import BinanceAPI
from graph.candle import Graph
from model.lrmodel import LinearModel
from positon.psymbol import Psymbol
import matplotlib.pyplot as plt
from model.loadmodel import LoadModel
from model.basemodel import BaseModel
from bot import Bot
from log.log import Log

print('to display commands, type **help')

bncapi = BinanceAPI('GMT')
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
            gr = Graph(klines, commandSplit[1])
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
    if commandSplit[0] == "**info":
        infoSymbol = commandSplit[1]
        lm = LoadModel(infoSymbol, 'LR')
        print(lm.Model.Info)
    if commandSplit[0] == "**help":
        print("**drawgraph-SYMBOL (example->drawgraph-ETHBUSD) shows candle stick graph of symbol")
        print("**learn-SYMBOL (example->learn-ETHBUSD) learn model of symbol")
        print("**runbot to run bot(symbols must be learnt before use)")
        print("**data-SYMBOL(example->**data-ETHBUSD) shows klines of symbol in dataframe")
        print("**info-SYMBOL to get info about symbol")
        print("**exit kills program")