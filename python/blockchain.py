blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [0]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_amount():
    return float(input("Your transaction amount please: "))


def get_user_choice():
    return input("Your choice: ")


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print("-" * 20)


def verify_chain():
    if len(blockchain) > 1:
        for i in range(1, len(blockchain)):
            if blockchain[i][0] != blockchain[i - 1]:
                return False
    return True


wait_for_input = True

while wait_for_input:
    print("Choose Option:")
    print("  a: Add transaction amount")
    print("  p: Print chain")
    print("  m: Manipulate chain")
    print("  q: Quit")
    choice = get_user_choice()
    if choice == "a":
        add_transaction(get_transaction_amount(), get_last_blockchain_value())
    elif choice == "p":
        print_blockchain_elements()
    elif choice == "m":
        if len(blockchain) >= 1:
            blockchain[0] = [-1]
        if not verify_chain():
            print("INVALID CHAIN!!!\nDone!")
            print_blockchain_elements()
            wait_for_input = False
    else:
        continue

    if not verify_chain():
        print("INVALID CHAIN!!!\nDone!")
        print_blockchain_elements()
        wait_for_input = False
