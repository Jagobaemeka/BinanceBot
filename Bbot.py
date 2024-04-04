from binance.client import Client 
## from decouple import config
import pandas as pd
import pandas_ta as ta
import json
import os
import time
import sys
import datetime


api_key = 'ALsgaJ0YT0aLV0GrRLzE9V7zNMDGvpMJmfg1iTit6oHGibcebwi27FO6HoPAw6zi'
api_secret = 'ZDQzixxr21pO1LYUt8ntCbZ2P5uL0PufBppGdN32R1vEtU8rMFkfUlv21HSAEr2m'

asset ="BTCUSDT"
entry = 30 # Example value for entry
exit = 70 # Example value for exit



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

def log(msg):
    print(f"L0G: {msg}")
    if not os.path.isdir("logs"):
        os.mkdir("logs")


    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    time = now.strftime("%Y-%m-%d")

    with open(f"logs/{today}.txt", "a+") as log_file:
        log_file.write(f"{time} : {msg}\n")

rsi = get_rsi(asset)
old_rsi = rsi 


while True:

    try:

        if not os.path.exists("bot_account.json"):
            create_account()

        with open("bot_account.json") as f:
                account = json.load(f)

        print(account)


        old_rsi = rsi
        rsi = get_rsi(asset)

        if account["is_buying"]:

            if rsi < entry and old_rsi > entry:
                pass
                #do trade   

        else:
            
            if rsi > exit and old_rsi < exit:
                pass
                #do trade
    
        time.sleep(10)
        pass
    except Exception as e:
        log("ERROR" + str(e) )
        #log error
             
