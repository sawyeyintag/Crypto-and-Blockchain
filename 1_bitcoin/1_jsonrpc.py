'''  'bitcoind' may be started with authentication using user/password. Using json-rpc 
bitcoind -regtest -server -rpcuser=john -rpcpassword=hello
bitcoin-cli -regtest -rpcuser=john -rpcpassword=hello getblockchaininfo 

# The port 18443 is primary use for Json-rpc over HTTP.
curl --user john:hello  --data-binary "{\"jsonrpc\": \"1.0\", \"id\":\"1\", \"method\": \"getblockchaininfo\", \"params\": [] }" -H "content-type: text/plain;" http://127.0.0.1:18443/

# Alternatively the bitcoind parameters can be add to:
	 C:/mycrypto/etc/Bitcoin/bitcoin.conf
server=1
regtest=1
rpcuser=john
rpcpassword=hello
rpcallowip=127.0.0.1     ## Optional
rpcport=18443            ## Default(main): 8332, testnet: 18332
'''
##############################################################

## pip install requests
## Using start_bitcoin_qt.bat

import requests
def json_rpc(URL, DATA):
    HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(URL, data=DATA, headers=HEADERS).text

## URL: "http://{USER}:{PWD}@{HOST}:{PORT}"
URL =   'http://john:hello@127.0.0.1:18443'
METHOD = 'getblockchaininfo'   ## Try: 'getblockcount'
DATA = '{"jsonrpc":"2.0", "method": "%s","params": [], "id": 1}' % METHOD
res = json_rpc(URL, DATA)
print(res)

import json
def json_test():
   js = json.loads(res)   	# str -> json
   print(js['result'])
   print(js['result']['chain'])
   print(js['result']['blocks'])
# json_test()

#------------------------------------------------

'''   Blockchain gateways
Ex. 'getblock.io' is a gateway that support both JSON RPC and Web Api.
https://getblock.io/
	Get a free endpont: email (Authen with Google). 
		Protocol: Bitcoin
		Network: Testnet
		API interrface: Json-rpc
https://go.getblock.io/baddeb10abff4800b37b0919908e7745

Try: another Endpoints:
		Protocol: Ethereum
		Network: sepolia
'''
URL = "https://go.getblock.io/baddeb10abff4800b37b0919908e7745"
# print(json_rpc(URL, DATA))



