import hashlib
from urllib.parse import quote as url_quote

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': self.get_current_time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'người gửi': sender,
            'người nhận': recipient,
            'số tiền': amount,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def get_current_time(self):
        from time import time
        return time()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            prev_block = self.chain[i - 1]
            if block['previous_hash'] != self.hash(prev_block):
                return False
            if not self.is_proof_valid(prev_block['proof'], block['proof']):
                return False
        return True

    def hash(self, block):
        block_string = str(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    def is_proof_valid(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

print("Chào mừng đến với ứng dụng Blockchain!")