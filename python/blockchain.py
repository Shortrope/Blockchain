blockchain = [[]]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_amount():
    return float(input("Your transaction amount please: "))


def get_user_choice():
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print(block)


while True:
    print("Choose Option:")
    print("  a: Add transaction amount")
    print("  o: Output chain")
    print("  q: Quit")
    choice = get_user_choice()
    if choice == "a":
        add_value(get_transaction_amount(), get_last_blockchain_value())
    elif choice == "o":
        print_blockchain_elements()
    else:
        break
