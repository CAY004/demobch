from flask import Flask, render_template, request, jsonify
from blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index.html', blockchain=blockchain.chain)

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.add_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.mine(previous_hash)
    response = {
        'message': 'New block mined',
        'index': block.index,
        'transactions': block.transactions,
        'previous_hash': previous_hash,
        'nonce': block.nonce,
        'timestamp': block.timestamp,
    }
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=8080)