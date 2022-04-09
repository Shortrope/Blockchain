import unittest

import blockchain as bc


class TestBlockchain(unittest.TestCase):
    def test_initial_blockchain(self):
        bc.blockchain = []
        self.assertEqual([], bc.blockchain)

    def test_get_last_transaction_of_empty_blockchain(self):
        bc.blockchain = []
        self.assertEqual(0, len(bc.blockchain))
        self.assertIsNone(bc.get_last_transaction())

    def test_get_last_transaction_with_one_entry(self):
        bc.blockchain = [[[0], 1]]
        self.assertListEqual([[0], 1], bc.get_last_transaction())

    def test_get_last_transaction_with_multiple_entries(self):
        bc.blockchain = [[[0], 1.0], [[[0], 1.0], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertListEqual([[[[0], 1.0], 2.0], 3.0], bc.get_last_transaction())

    def test_verify_empty_chain(self):
        bc.blockchain = []
        self.assertTrue(bc.verify_chain())

    def test_verify_chain_w_single_entry(self):
        bc.blockchain = [[[0], 1]]
        self.assertTrue(bc.verify_chain())

    def test_verify_good_chain_w_multiple_entries(self):
        bc.blockchain = [[[0], 1], [[[0], 1], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertTrue(bc.verify_chain())

    def test_verify_bad_chain_w_multiple_entries(self):
        bc.blockchain = [[[1], 1], [[[0], 1], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertFalse(bc.verify_chain())
        bc.blockchain = [[[0], 1.1], [[[0], 1], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertFalse(bc.verify_chain())
        bc.blockchain = [[[0], 1], [[[0], 1.1], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertFalse(bc.verify_chain())
        bc.blockchain = [[[0], 1], [[[0], 1], 2.0], [[[[1], 1.0], 2.0], 3.0]]
        self.assertFalse(bc.verify_chain())

    def test_add_transaction_to_open_transactions_list(self):
        bc.open_transactions = []
        bc.add_transaction("Josie", "Mak", 2.2)
        expected = [{"sender": "Mak", "recipient": "Josie", "amount": 2.2}]
        self.assertListEqual(expected, bc.open_transactions)
        bc.add_transaction("Rosie", "Mak", 3.3)
        expected = [
            {"sender": "Mak", "recipient": "Josie", "amount": 2.2},
            {"sender": "Mak", "recipient": "Rosie", "amount": 3.3},
        ]
        self.assertListEqual(expected, bc.open_transactions)


if __name__ == "__main__":
    unittest.main()
