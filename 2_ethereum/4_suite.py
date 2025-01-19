''' Truffle is an Ethereum development framework. It was very popular 
for smart contracts development, but built around JavaScript.

Brownie is a Python-based framework similar to Truffle, it will be
used in the topic of smart contracts.

Later trufflesuite.com introduced Ganache a Python-based local 
Ethereum blockchain for development and testing, so that we
do not need Geth or infura.

# Download and Install:
	https://trufflesuite.com/ganache/
    		Ganache-x.y.z-win-x64.appx

# Start Ganache GUI.
     	Quickstart Ethereum
   10 addresses with 100 Eth balance are automatic generated.	
	Change port 7545 -> 8545 (Setting -> Server)

-----------------------------------
## Test Ganache with Geth console
geth attach http://127.0.0.1:8545
web3.version
eth.accounts     ## Check with Ganache.
addr = "0x50f118fa92fE19501F1d0F78471dCAcfc2a2c18f"
eth.getBalance(addr)
exit
-----------------------------------   '''

## 'ganache' supports both json_rpc and web3.py.
from web3 import Web3
URL = 'http://127.0.0.1:8545'

w3 = Web3(Web3.HTTPProvider(URL))
# print(w3.client_version)
# print(w3.eth.accounts)

addr = "0x50f118fa92fE19501F1d0F78471dCAcfc2a2c18f"
# print(w3.eth.get_balance(addr))

## Ganache creates new accounts and resets balances by default when started.
## Try: Save a workspace and reload to avoid resetting.

## Ganache doesn't update account balances immediately or even a new block is mined.
## The simplest solution is to restart Ganache with the saved workspace.

#############################################################

''' Foundry is a tool set for writing, testing, and deploying smart contracts. 
Anvil is a local Ethereum node written in Rust similar to Ganache.
	https://book.getfoundry.sh/anvil/index.html

## Download:
	https://github.com/foundry-rs/foundry/releases

## Unzip to:
 	C:/mycrypto/etc/Foundry

## Set Path: 
	set PATH=%PATH%;C:/mycrypto/etc/Foundry

anvil -V
anvil -help

## Start default anvil: 10 accounts with 10000 eth each.
anvil		

## Start with specific account number and balance
anvil --accounts 3 --balance 10

## Default Listening on 127.0.0.1:8545
## Anvil accepts checksum addresses.
--------------------------------------------

## Test Anvil with Geth console
setp
geth attach http://127.0.0.1:8545
web3.version
eth.accounts 
exit
-------------------------------------------- '''

from web3 import Web3
URL = 'http://127.0.0.1:8545'

w3 = Web3(Web3.HTTPProvider(URL))
# print(w3.client_version)
# print(w3.eth.accounts)

## Anvil accepts only checksum addresses.
addr = Web3.to_checksum_address("0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266")
print(w3.eth.get_balance(addr))

'''
------------------------------------------------

## Cast: is tool for command line to interact with local or 
remote Ethereum nodes without writing codes.
	https://book.getfoundry.sh/cast/index.html

setav.bat
cast -help

'cast' sends command to 127.0.0.1:8545 by default.
	cast <command> --<option> <args>
cast client
cast chain-id
cast block-number
cast block 0
cast age --block 0
cast gas-price
cast rpc eth_accounts    # Send rpc command.

set ADDR=0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266
cast balance %ADDR%

## 'cast' may send command to remote nodes.
set URL=https://sepolia.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558
cast client --rpc-url %URL%

## Check balance of a sepolia address.
set ADDR=0xa6f85eE31499b8CB45EE77049AC201d5dccbf8D5
cast balance %ADDR% --rpc-url %URL%
'''
