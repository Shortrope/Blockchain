blockchain = [[]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    return float(input("Your transaction amount please: "))


add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())
add_value(get_user_input(), get_last_blockchain_value())

for block in blockchain:
    print(block)
