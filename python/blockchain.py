blockchain = []
open_transactions = []
owner = "Mak"


def get_last_transaction():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {"recipient": recipient, "sender": sender, "amount": amount}
    open_transactions.append(transaction)


def get_transaction():
    sender = owner
    recipient = input("Who is the recipient? ")
    amount = float(input("Your transaction amount: "))
    return recipient, sender, amount


def get_user_choice():
    return input("Your choice: ")


def print_blockchain_elements():
    output = ""
    # output = ", ".join(map(str, blockchain))
    # output += "\n" + ("-" * 20)
    for block in blockchain:
        output += f"\n{block}"
    print(output)


def verify_chain():
    if len(blockchain) > 1:
        for i in range(1, len(blockchain)):
            if blockchain[i][0] != blockchain[i - 1]:
                return False
    return True


def main():
    wait_for_input = True

    while wait_for_input:
        print("Choose Option:")
        print("  a: Add transaction amount")
        print("  p: Print chain")
        print("  m: Manipulate chain")
        print("  q: Quit")
        choice = get_user_choice()
        if choice == "a":
            recipient, sender, amount = get_transaction()
            add_transaction(recipient, sender, amount)
            print(open_transactions)
        elif choice == "p":
            print_blockchain_elements()
        elif choice == "m":
            if len(blockchain) >= 1:
                blockchain[0] = [-1]
        elif choice == "q":
            break
        else:
            continue

        if not verify_chain():
            print("INVALID CHAIN!!!\nDone!")
            print_blockchain_elements()
            wait_for_input = False


if __name__ == "__main__":
    main()
