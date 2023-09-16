from binanceapi.binanceapi import BinanceAPI
from positon.psymbol import Psymbol

class Position:
    def __init__(self, symbol : Psymbol):
        self.__PSymbol = symbol
        self.__BinanceAPI = BinanceAPI('GMT')

    def EnterPosition(self):
        self.__BinanceAPI.Buy(symbol=self.__PSymbol.Symbol)

    def ExitPosition(self, type:str):
        self.__BinanceAPI.Sell(symbol=self.__PSymbol.Symbol)

    @property
    def PSymbol(self):
        return self.__PSymbol

        
