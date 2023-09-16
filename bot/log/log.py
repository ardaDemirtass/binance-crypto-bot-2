from positon.psymbol import Psymbol
from datetime import datetime

class Log:
    def __init__(self, symbol : Psymbol):
        self.__Symbol = symbol

    def ExitLog(self, exitPrice):
        if self.__Symbol.TargetPrice <= exitPrice:
            text = f"""
***EXIT LOG***
*PROFIT*
SYMBOL : {self.__Symbol.Symbol}
ENTER PRICE : {self.__Symbol.EnterPrice}
TARGET PRICE : {self.__Symbol.TargetPrice}
STOP PRICE : {self.__Symbol.StopPrice}
SOLD AT : {exitPrice}
DATE : {datetime.now()}
---------------
                """
        else:
            text = f"""
***EXIT LOG***
*LOSS*
SYMBOL : {self.__Symbol.Symbol}
ENTER PRICE : {self.__Symbol.EnterPrice}
TARGET PRICE : {self.__Symbol.TargetPrice}
STOP PRICE : {self.__Symbol.StopPrice}
SOLD AT : {exitPrice}
DATE : {datetime.now()}
---------------
                """
        text_file = open("log/log.txt", "a")
        text_file.write(text + '\n')
        text_file.close()  

    def EnterLog(self):
        text = f"""
***ENTER LOG***
SYMBOL : {self.__Symbol.Symbol}
ENTER PRICE : {self.__Symbol.EnterPrice}
TARGET PRICE : {self.__Symbol.TargetPrice}
STOP PRICE : {self.__Symbol.StopPrice}
DATE : {datetime.now()}
---------------
                """
        text_file = open("log/log.txt", "a")
        text_file.write(text + '\n')
        text_file.close()
    