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

    def test_add_tranasaction_to_empty_chain(self):
        bc.blockchain = []
        bc.add_transaction(1)
        expected = [[0], 1]
        self.assertListEqual(expected, bc.get_last_transaction())

    def test_add_tranasaction_to_populated_chain(self):
        bc.blockchain = [[[0], 1]]
        bc.add_transaction(2.0)
        expected = [[[0], 1], [[[0], 1], 2.0]]
        self.assertListEqual(expected, bc.blockchain)
        bc.add_transaction(3.0)
        expected = [[[0], 1], [[[0], 1], 2.0], [[[[0], 1.0], 2.0], 3.0]]
        self.assertListEqual(expected, bc.blockchain)

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


if __name__ == "__main__":
    unittest.main()
