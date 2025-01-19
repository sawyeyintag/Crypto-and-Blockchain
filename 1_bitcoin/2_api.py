## pip install python-bitcoinrpc  Check: python 3.9+ and dependency conflicts 
## Using start_bitcoin_qt.bat

## Using API:
from bitcoinrpc.authproxy import AuthServiceProxy
api = AuthServiceProxy('http://john:hello@127.0.0.1:18443')
#  print(api.getblockchaininfo())
# print(api.getblockhash(0)) 

#------------------------------------------------------

''' 'tatum.io' is a provider that supports access to 60+ blockchains 
(e.g., Bitcoin, Ethereum, Solana, Binance Smart Chain, Polygon).

Register: https://tatum.io
Create a Testnet API key:  '''

## Using Restful URL:
API_KEY = 'c5f29e5b-8ee1-4111-8717-6e797fa56673'
HEADERS = {'Content-type': 'application/json', 'x-api-key': API_KEY }

import json
def print_json(res):
   print(json.dumps(res.json(), indent=4, sort_keys=True))

import requests
from pprint import pprint
def get_info():
   URL = 'https://api.tatum.io/v3/bitcoin/info'
   print_json(requests.get(URL, headers=HEADERS))
# get_info()
###########################################################

## Ex. Get block hash by block number.
def get_block_hash(num):
   URL = "https://api.tatum.io/v3/bitcoin/block/hash/" + num 
   print(requests.get(URL, headers=HEADERS).json())
# get_block_hash('0')   ## The genesis block of testnet.
hash = '000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943'

## Ex. Get block by hash.
def get_block():
   URL = "https://api.tatum.io/v3/bitcoin/block/" + hash 
   print_json(requests.get(URL, headers=HEADERS))
# get_block()        ## The receiver address
addr = 'mpXwg4jMtRhuSpVq4xS3HFHmCmWp9NyGKt'

## Ex. Get balance of an address.
def get_balance(address):
   URL = "https://api.tatum.io/v3/bitcoin/address/balance/" + address
   print_json(requests.get(URL, headers=HEADERS))
# get_balance(addr)
