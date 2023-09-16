class Psymbol:
    def __init__(self, symbol : str, enterPrice : float, targetPrice : float, stopPrice : float):
        self.__Symbol = symbol
        self.__EnterPrice = enterPrice
        self.__TargetPrice = targetPrice
        self.__StopPrice = stopPrice

    @property
    def Symbol(self):
        return self.__Symbol
    
    @property
    def EnterPrice(self):
        return self.__EnterPrice
    
    @property
    def TargetPrice(self):
        return self.__TargetPrice
    
    @property
    def StopPrice(self):
        return self.__StopPrice