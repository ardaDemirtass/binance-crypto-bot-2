import pandas as pd
from sklearn.linear_model import LinearRegression
from model.basemodel import BaseModel
import os
import pickle

class LinearModel(BaseModel):
    def __init__(self, symbol: str, input: pd.DataFrame, output: pd.DataFrame):
        super().__init__(symbol, input, output)
        self.__lr = LinearRegression()

    def CreateModel(self):
        self.__lr.fit(self.Xtrain, self.Ytrain)

    def SaveModel(self):
        if not os.path.exists(f"savedsymbols/{self.Symbol}"):
            os.mkdir(f"savedsymbols/{self.Symbol}")
        modelFileName = f"savedsymbols/{self.Symbol}/LR.pickle"
        if os.path.isfile(modelFileName):
            os.remove(modelFileName)
        pickle.dump(self, open(modelFileName, "wb"))

    def Predict(self, pred):
        return self.__lr.predict(pred)
    
    def DeleteModel(self):
        try:
            os.remove(f'savedsymbols/{self.Symbol}')
        except:
            pass

    @property
    def Lr(self):
        return self.__lr