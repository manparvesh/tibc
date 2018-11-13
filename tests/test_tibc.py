from tibc import Blockchain
from unittest import TestCase

block_one_transactions = {"sender": "Alice", "receiver": "Bob", "amount": "50"}
block_two_transactions = {"sender": "Bob", "receiver": "Cole", "amount": "25"}
block_three_transactions = {"sender": "Alice", "receiver": "Cole", "amount": "35"}
fake_transactions = {"sender": "Bob", "receiver": "Cole, Alice", "amount": "25"}


class TestSample(TestCase):
    """
        Test our tiny blockchain
    """

    def __init__(self, methodName='runTest'):
        super(TestSample, self).__init__()

    def runTest(self):
        local_blockchain = Blockchain()
        local_blockchain.print_blocks()

        local_blockchain.add_block(block_one_transactions)
        local_blockchain.add_block(block_two_transactions)
        local_blockchain.add_block(block_three_transactions)
        local_blockchain.print_blocks()
        self.assertTrue(local_blockchain.validate_chain())

        local_blockchain.chain[2].transactions = fake_transactions
        self.assertFalse(local_blockchain.validate_chain())
