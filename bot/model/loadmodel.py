import pandas as pd
import numpy as np
import pickle
from model.basemodel import BaseModel

class LoadModel:
    def __init__(self, symbol : str, reg : str):
        self.__Symbol = symbol
        self.__Reg = reg
        self.__Model : BaseModel
        self.__LoadModel()

    def __LoadModel(self):
        with open(f'savedsymbols/{self.__Symbol}/{self.__Reg}.pickle', 'rb') as f:
            self.__Model = pickle.load(f)

    @property
    def Reg(self):
        return self.__Reg
    
    @property
    def Symbol(self):
        return self.__Symbol
    
    @property
    def Model(self):
        return self.__Model