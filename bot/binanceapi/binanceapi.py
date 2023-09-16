from binance.client import Client
import requests
import pandas as pd
import requests
import json


class BinanceAPI:
    def __init__(self, timezone : str):
        self.__TimeZone = timezone
        self.__ApiKey = ''
        self.__ApiSecret = ''
        self.__Client = Client(self.__ApiKey, self.__ApiSecret)

    def GetHistoricalKlines(self, symbol):
        klines = self.__Client.get_historical_klines(symbol,Client.KLINE_INTERVAL_1DAY, f'365 day ago {self.__TimeZone}')
        tdf = pd.DataFrame(data=range(1,366), columns=['day'])
        df = pd.DataFrame(data=klines, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'], index=range(0,365))
        dfconcat = pd.concat([tdf, df], axis=1)
        dfconcat = dfconcat.drop(['quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol','takerBuyQuoteVol', 'ignore', 'dateTime','closeTime', 'volume'], axis=1)
        dfconcat['open'] = dfconcat['open'].astype(float)
        dfconcat['close'] = dfconcat['close'].astype(float)
        dfconcat['high'] = dfconcat['high'].astype(float)
        dfconcat['low'] = dfconcat['low'].astype(float)
        return dfconcat
    
    def GetCurrentPrice(self, symbol):
        key = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        data = requests.get(key)
        data = data.json()
        return float(data['price'])
    
    def AssetBalance(self, symbol):
        return self.__Client.get_asset_balance(asset=symbol)
    
    def Buy(self, symbol):
        order = self.__Client.order_market_buy(
            symbol=symbol,
            quantity=self.CalcQuantity(symbol=symbol)
        )
        return order
    
    def Sell(self, symbol):
        order = self.__Client.order_limit_sell(
            symbol=symbol,
            quantity=self.AssetBalance(symbol=symbol)
        )
        return order
    
    def CalcQuantity(self, symbol):
        return self.AssetBalance(symbol='BUSD') / self.GetCurrentPrice(symbol=symbol)
    