from model.loadmodel import LoadModel
from model.basemodel import BaseModel
from model.lrmodel import LinearModel
from binanceapi.binanceapi import BinanceAPI
from positon.psymbol import Psymbol
from positon.position import Position
import time
from log.log import Log

class Bot:
    def __init__(self, symbols):
        self.__Symbols = symbols
        self.__Models = []
        self.__LoadModels()
        self.__InPosition = False
        self.__PSymbol : Psymbol
        self.__Position : Position
        self.__BinanceAPI = BinanceAPI('GMT')
        self.__Log : Log

    def __LoadModels(self):
        for symbol in self.__Symbols:
            lm = LoadModel(symbol, 'LR')
            self.__Models.append(lm.Model)

    def __SearchForPosition(self):
        for model in self.__Models:
            prediction = model.Predict(model.XPredict)
            currentPrice = self.__BinanceAPI.GetCurrentPrice(model.Symbol)
            rate = (prediction - currentPrice) / currentPrice
            print("*****")
            print(f"symbol : {model.Symbol}")
            print(f"current price : {currentPrice}")
            print(f"estimated close : {prediction}")
            print(f"rate to goal : {rate}")
            print("*****")
            if rate >= 101/100:
                enterPrice = currentPrice
                targetPrice = currentPrice + rate
                stopPrice = currentPrice - rate
                self.__PSymbol = Psymbol(symbol=model.Symbol,enterPrice=enterPrice, targetPrice=targetPrice, stopPrice=stopPrice)
                self.__Position = Position(self.__PSymbol)
                self.__Position.EnterPosition()
                self.__InPosition = True
                self.__Log = Log(self.__PSymbol)
                self.__Log.EnterLog()
                break

    def __ManagePosition(self):
        currentPrice = self.__BinanceAPI.GetCurrentPrice(self.__Position.PSymbol.Symbol)
        if currentPrice >= self.__Position.PSymbol.TargetPrice:
            self.__Position.ExitPosition("target")
            self.__InPosition = False
            self.__Log.ExitLog(currentPrice)

        if currentPrice < self.__Position.PSymbol.StopPrice:
            self.__Position.ExitPosition("stop")
            self.__InPosition = False
            self.__Log.ExitLog(currentPrice)

        print("*****")
        print(f"symbol : {self.__Position.PSymbol.Symbol}")
        print(f"current price : {currentPrice}")
        print(f"target price : {self.__Position.PSymbol.TargetPrice}")
        print(f"stop price : {self.__Position.PSymbol.StopPrice}")
        print("*****")

    def RunBot(self):
        while True:
            if self.__InPosition == False:
                self.__SearchForPosition()
            else:
                self.__ManagePosition()
            time.sleep(1)