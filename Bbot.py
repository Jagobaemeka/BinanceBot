from binance.client import Client 
## from decouple import config 


api_key = 'ALsgaJ0YT0aLV0GrRLzE9V7zNMDGvpMJmfg1iTit6oHGibcebwi27FO6HoPAw6zi'
api_secret = 'ZDQzixxr21pO1LYUt8ntCbZ2P5uL0PufBppGdN32R1vEtU8rMFkfUlv21HSAEr2m'

Client = Client(api_key, api_secret, testnet=True )

balance = Client.get_asset_balance(asset = "BTC")

print(balance)
