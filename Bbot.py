from binance.client import Client 
## from decouple import config
import pandas as pd
import pandas_ta as ta
import json


api_key = 'ALsgaJ0YT0aLV0GrRLzE9V7zNMDGvpMJmfg1iTit6oHGibcebwi27FO6HoPAw6zi'
api_secret = 'ZDQzixxr21pO1LYUt8ntCbZ2P5uL0PufBppGdN32R1vEtU8rMFkfUlv21HSAEr2m'

Client = Client(api_key, api_secret, testnet=True )

balance = Client.get_asset_balance(asset = "BTC")

def fetch_klines(asset):


    klines = Client.get_historical_klines(asset, Client.KLINE_INTERVAL_1MINUTE,"1 hour AGO utc")

    klines = [ [x[0], float(x[4]) ] for x in klines ]

    klines = pd.DataFrame(klines, columns = ["time", "price"])
    klines["time"] = pd.to_datetime(klines["time"], unit = "ms")

    return klines

def get_rsi(asset):
    
    klines = fetch_klines(asset)
    klines["rsi"] = ta.rsi(close = klines["price"], lenght = 14)

    return klines["rsi"].iloc[- 1]

def create_account():

    account = {
            "is_buying":True,
            "assets":{},
            }


    with open("bot_account.json","w") as f:
        f.write(json.dumps(account))



create_account()
