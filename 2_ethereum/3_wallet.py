## Creating a Sepolia Wallet with Web3.py
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.org"))

## Create a new account
def get_account(): 
   ac = w3.eth.account.create()
   print("Wallet Address:", ac.address)
   print("Private Key:", ac.key.hex())
# get_account()   
## Wallet Address: 0xB62752b3A1B456E7b47C396A43EE9BDFfA6CAa29
## Private Key: 235a826aa18efa57a395be8572e0bbdb93d9ebde17a62de9941c8052ff40c449

''' Sepolia Testnet Faucet:
Getting free 0.05 eth from 
https://cloud.google.com/application/web3/faucet/ethereum/sepolia
Recipient:
  0xB62752b3A1B456E7b47C396A43EE9BDFfA6CAa29
Transaction hash:  
  0xb3587bc5d9c8ccfe12b15b8d017c15343eab968e81c7f8fb7aa432a77c6df379
'''
from web3 import Web3
URL = "https://sepolia.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558"
web3 = Web3(Web3.HTTPProvider(URL))

def is_connected(): 
    if web3.is_connected():
        print("Connected to Sepolia network")
    else:
        print("Failed to connect to Sepolia network")
# is_connected()

## Checking the Wallet Balance
def get_balance(addr): 
    wei = web3.eth.get_balance(addr)
    ## Convert Wei to Ether
    eth = web3.from_wei(wei, 'ether')
    print(f"Wei: {wei}\nEth: {eth}")
addr = '0xB62752b3A1B456E7b47C396A43EE9BDFfA6CAa29'
get_balance(addr)

## Checking the Transaction
def get_tx(tx_hash):
    try:
        tx = web3.eth.get_transaction(tx_hash)
        # print(tx)
        eth = web3.from_wei(tx['value'], 'ether')
        print(f"{eth} ETH")
    except Exception as ex:
        print(ex)
tx_hash = '0xb3587bc5d9c8ccfe12b15b8d017c15343eab968e81c7f8fb7aa432a77c6df379'
# get_tx(tx_hash)

################################################################

''' 'tatum.io' is a platform that provides connections for multiple blockchains,
 including Bitcoin, Ethereum, Solana, Polygon, and many others.
It supports development tools and APIs for developing blockchain applications.
Go to https://tatum.io/ and sign up for API_KEY:  '''

API_KEY = 'c5f29e5b-8ee1-4111-8717-6e797fa56673'
CHAIN = 'ethereum-sepolia'

## API_KEY may be in path params.
# URL = 'https://api.tatum.io/v3/blockchain/node/%s/%s?type=testnet' % (CHAIN, API_KEY)
# HEADERS = {'Content-type': 'application/json' }

## API_KEY may be in headers.
URL = 'https://api.tatum.io/v3/blockchain/node/%s?type=testnet' % CHAIN
HEADERS = {'Content-type': 'application/json', 'x-api-key': API_KEY }

## 'tatum.io' supports json-rpc.
import requests
def client_version():
   DATA = '{"jsonrpc":"2.0", "method": "web3_clientVersion","params": [], "id": 1}'
   res = requests.post(URL, data=DATA, headers=HEADERS)
   # print(res.text)
   print(res.json()['result'])
# client_version()

## 'tatum.io' also supports restfull apis.
def get_balance(addr):             ## Using GET (no DATA)
   URL = "https://api.tatum.io/v3/ethereum/account/balance/" + addr
   res =  requests.get(URL, headers=HEADERS).json()
   print(res['balance'])

## Suppose we have wallet addresses:
addr = '0xB62752b3A1B456E7b47C396A43EE9BDFfA6CAa29'
# get_balance(addr)

## Get tx by hash
def get_tx(hash):
   URL = 'https://api.tatum.io/v3/data/transactions/hash?chain='+ CHAIN +'&hash=' + hash
   res =  requests.get(URL, headers=HEADERS).json()
   print(res)

## Suppose we have a tx hash.
tx_hash = '0xb3587bc5d9c8ccfe12b15b8d017c15343eab968e81c7f8fb7aa432a77c6df379'
# get_tx(tx_hash)
## Different platforms may implement tx differently.

#------------------------------------------------------------

''' https://moralis.io
Moralis dashboard: https://admin.moralis.io/
Register: https://admin.moralis.io/register
'''
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub25jZSI6IjVjYmFmMGJiLTkxM2QtNGU4MS1hYmIyLTdjZTNmOWE1ZjNhMSIsIm9yZ0lkIjoiMTE2MjYyIiwidXNlcklkIjoiMTE1OTA4IiwidHlwZUlkIjoiNTIyODQwM2EtNzBkYy00ZTkwLTlkOGItY2Q1OGVmYmU0OTc5IiwidHlwZSI6IlBST0pFQ1QiLCJpYXQiOjE2ODQzMDU0NzgsImV4cCI6NDg0MDA2NTQ3OH0.-EHM2YWgKswhzhPaJiQmE-0DuxWYQP3mW5JaxdFTo_Y'

## https://moralisweb3.github.io/Moralis-Python-SDK/
## pip install moralis
from moralis import utils
# print(utils.web3_api_version(api_key=API_KEY))

## Moralis offers service via the EVM API.
from moralis import evm_api
def get_balance(addr):
    print(evm_api.balance.get_native_balance(
        api_key=API_KEY,
        params={
            "address": addr,
            "chain": "sepolia",
        },
    ))
addr = '0xB62752b3A1B456E7b47C396A43EE9BDFfA6CAa29'   
get_balance(addr)
# "0xa6f85eE31499b8CB45EE77049AC201d5dccbf8D5"





