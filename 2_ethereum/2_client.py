## Using Json-rpc with Geth.
## start_geth.bat
URL = 'http://127.0.0.1:8545'
HEADERS = {'Content-type': 'application/json'}
import requests
def json_rpc(method):
   DATA = '{"jsonrpc":"2.0", "method": "%s","params": [], "id": 1}' % method
   # print(DATA)
   return requests.post(URL, data=DATA, headers=HEADERS).text

print(json_rpc('web3_clientVersion'))
# print(json_rpc('eth_syncing'))

## Try: These are methods without parameters.
##    net_version  network ID (e.g., 1 for mainnet, 5 for Goerli). 
##    net_peerCount  number of peers currently connected.
##    net_listening  if listening for network connections.
##    eth_syncing    items being synced.
##    eth_blockNumber  number of the most recent block.
##    eth_gasPrice  current price per gas in wei.
##    eth_mining   if the node is actively mining new blocks.
#--------------------------------------------------------

## Using Web3 with Geth.
## pip install --upgrade setuptools
## pip install web3
from web3 import Web3
URL = 'http://127.0.0.1:8545'

w3 = Web3(Web3.HTTPProvider(URL))
# print(w3.client_version)
# print(w3.is_connected())
# print(w3.eth.chain_id)      ## 11155111 is sepolia. 
# print(w3.eth.gas_price)

#### Working with blocks
# print(w3.eth.block_number)    ## Get most recent block number
# print(w3.eth.get_block(0))    ## Get block by number Try: 'latest'
# print(w3.eth.gas_price)       ## wei.

## Can't do much here since we don't have have any ETH yet.
## https://web3py.readthedocs.io/en/stable/
## https://blog.logrocket.com/web3-py-tutorial-guide-ethereum-blockchain-development-with-python/

## Geth takes too long to download its blockchain.
## There are a lot of public nodes that offer free connection points.

#------------------------------------------------------------
''' Let's try: infura.io
'infura.io' provides gateway to many public Ethereum Blockchain.
Register: https://infura.io
Api Key:    86bf0e4aba984b6e9da45dc3df569558

Create URL using Api Key.
## To  Ethereum 'main' net.
https://mainnet.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558

## To 'sepolia' test net. 
https://sepolia.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558

## There are many gate ways like this ex.
Using getblock.io to connect to sepolia.
URL = "https://eth.getblock.io/a3ac0ff5-7c75-417e-ac5d-143b256568d2/sepolia/"
'''
from web3 import Web3
URL = "https://sepolia.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558"
w3 = Web3(Web3.HTTPProvider(URL))
print(w3.client_version)
# print(w3.eth.chain_id)
# print(w3.eth.accounts)      ## [] 
           ## Infura is not a wallet and does not support mining.

## Suppose we have a wallet address.
addr = '0xa6f85eE31499b8CB45EE77049AC201d5dccbf8D5'
# print(w3.eth.get_balance(addr))


