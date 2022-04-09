import unittest
from tkinter import W

import blockchain as bc


class TestBlockchain(unittest.TestCase):
    tx1 = {"sender": "Mak", "recipient": "Josie", "amount": 1.1}
    tx2 = {"sender": "Mak", "recipient": "Rosie", "amount": 2.2}
    tx3 = {"sender": "Mak", "recipient": "Sosie", "amount": 3.3}
    open_tx1 = [tx1]
    open_tx2 = [tx1, tx2]
    bc_with_one_transaction = [
        {"previous_hash": "", "index": 0, "transactions": []},
        {
            "previous_hash": "0[]",
            "index": 1,
            "transactions": [{"recipient": "Josie", "sender": "Mak", "amount": 1.1}],
        },
    ]

    def test_initial_blockchain(self):
        bc.blockchain = [bc.genesis_block]
        expected = [{"previous_hash": "", "index": 0, "transactions": []}]
        self.assertEqual(expected, bc.blockchain)

    def test_get_last_transaction_of_initial_blockchain(self):
        bc.blockchain = [bc.genesis_block]
        self.assertEqual(1, len(bc.blockchain))
        expected = bc.genesis_block
        self.assertEqual(expected, bc.get_last_transaction())

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

    def test_get_last_transaction_with_one_entry(self):
        bc_with_one_transaction = [
            {"previous_hash": "", "index": 0, "transactions": []},
            {
                "previous_hash": "0[]",
                "index": 1,
                "transactions": [
                    {"recipient": "Josie", "sender": "Mak", "amount": 1.1}
                ],
            },
        ]
        bc.blockchain = bc_with_one_transaction
        expected = {
            "previous_hash": "0[]",
            "index": 1,
            "transactions": [{"recipient": "Josie", "sender": "Mak", "amount": 1.1}],
        }
        self.assertDictEqual(expected, bc.get_last_transaction())

    def test_verify_empty_chain(self):
        bc.blockchain = [bc.genesis_block]
        self.assertTrue(bc.verify_chain())

    def test_verify_chain_w_single_entry(self):
        bc_with_one_transaction = [
            {"previous_hash": "", "index": 0, "transactions": []},
            {
                "previous_hash": "0[]",
                "index": 1,
                "transactions": [
                    {"recipient": "Josie", "sender": "Mak", "amount": 1.1}
                ],
            },
        ]
        bc.blockchain = bc_with_one_transaction
        self.assertTrue(bc.verify_chain())

    def test_verify_good_chain_w_multiple_entries(self):
        bc_with_mult_transaction = [
            {"previous_hash": "", "index": 0, "transactions": []},
            {
                "previous_hash": "0[]",
                "index": 1,
                "transactions": [
                    {"recipient": "Josie", "sender": "Mak", "amount": 1.1}
                ],
            },
            {
                "previous_hash": "0[]1[{'recipient': 'Josie', 'sender': 'Mak', 'amount': 1.1}]",
                "index": 2,
                "transactions": [
                    {"recipient": "Rosie", "sender": "Mak", "amount": 2.2}
                ],
            },
            {
                "previous_hash": "0[]1[{'recipient': 'Josie', 'sender': 'Mak', 'amount': 1.1}]2[{'recipient': 'Rosie', 'sender': 'Mak', 'amount': 2.2}]",
                "index": 3,
                "transactions": [
                    {"recipient": "Sosie", "sender": "Mak", "amount": 3.3}
                ],
            },
        ]
        bc.blockchain = bc_with_mult_transaction
        self.assertTrue(bc.verify_chain())

    def test_verify_bad_chain_w_multiple_entries(self):
        bc_with_mult_transaction = [
            {"previous_hash": "", "index": 0, "transactions": []},
            {
                "previous_hash": "0[]",
                "index": 1,
                "transactions": [
                    {"recipient": "Josie", "sender": "Mak", "amount": 1.1}
                ],
            },
            {
                "previous_hash": "0[]1[{'recipient': 'Josie', 'sender': 'Mak', 'amount': 1.1}]",
                "index": 2,
                "transactions": [
                    {"recipient": "Rosie", "sender": "Mak", "amount": 777.77}
                ],
            },
            {
                "previous_hash": "0[]1[{'recipient': 'Josie', 'sender': 'Mak', 'amount': 1.1}]2[{'recipient': 'Rosie', 'sender': 'Mak', 'amount': 2.2}]",
                "index": 3,
                "transactions": [
                    {"recipient": "Sosie", "sender": "Mak", "amount": 3.3}
                ],
            },
        ]
        bc.blockchain = bc_with_mult_transaction
        self.assertFalse(bc.verify_chain())


if __name__ == "__main__":
    unittest.main()
