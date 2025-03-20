import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def test_blockchain_initialization(self):
        blockchain = Blockchain()
        self.assertEqual(len(blockchain.chain), 1)

if __name__ == '__main__':
    unittest.main()