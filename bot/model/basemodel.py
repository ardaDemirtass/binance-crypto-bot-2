from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self,symbol : str ,input : pd.DataFrame, output : pd.DataFrame, scale = True):
        self.__symbol = symbol
        self.__Input = input
        self.__Output = output
        self.__xtrain : np.array
        self.__xtest : np.array
        self.__ytrain : np.array
        self.__ytest : np.array
        self.__scx = StandardScaler()
        self.__scy = StandardScaler()
        self.__scaledx : np.array
        self.__scaledy : np.array
        self.__SplitTrainTest()
        self.__Scale()

    def __SplitTrainTest(self):
        self.__xtrain, self.__xtest, self.__ytrain, self.__ytest = train_test_split(self.__Input.iloc[0:364,:].values, self.__Output.iloc[0:364,:].values, test_size=0.3, random_state=0)

    def __Scale(self):
        self.__scaledx = self.__scx.fit_transform(self.__xtrain)
        self.__scaledy = self.__scy.fit_transform(self.__ytrain)

    @property
    def XPredict(self):
        return self.__Input.iloc[[364]].values.reshape(1,-1)

    @property
    def Symbol(self):
        return self.__symbol

    @property
    def Scx(self):
        return self.__scx
    
    @property
    def Scy(self):
        return self.__scy

    @property
    def Scaledx(self):
        return self.__scaledx
    
    @property
    def Scaledy(self):
        return self.__scaledy

    @property
    def Xtrain(self):
        return self.__xtrain
    
    @property
    def Xtest(self):
        return self.__xtest
    
    @property
    def Ytrain(self):
        return self.__ytrain
    
    @property
    def Ytest(self):
        return self.__ytest
    
    @property
    def Input(self):
        return self.__Input
    
    @property
    def Output(self):
        return self.__Output

    @abstractmethod
    def Predict(self):
        pass

    @abstractmethod
    def SaveModel(self):
        pass

    @abstractmethod
    def CreateModel(self):
        pass

    @abstractmethod
    def DeleteModel(self):
        pass
    