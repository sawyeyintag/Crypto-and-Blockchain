## pip install flask
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

URL = 'http://127.0.0.1:8545'  # Ganache or Anvil
# URL = "https://sepolia.infura.io/v3/86bf0e4aba984b6e9da45dc3df569558"

from web3 import Web3
w3 = Web3(Web3.HTTPProvider(URL))

@app.route('/getversion')
def get_version():
   return w3.client_version

@app.route('/getbalance', methods=['POST'])
def get_balance():
   addr = request.form.get('addr')
   return str(w3.eth.get_balance(addr))

@app.route('/getgasprice')
def get_gasprice():
   return str(w3.eth.gas_price)

if __name__ == '__main__':
    app.run(port=8080, debug=True)