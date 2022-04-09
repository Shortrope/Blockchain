from tkinter import W

genesis_block = {"previous_hash": "", "index": 0, "transactions": []}
blockchain = [genesis_block]
open_transactions = []
owner = "Mak"


def get_last_transaction():
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


def hash_block(block):
    # print("".join([str(block[k]) for k in block]))
    return "".join([str(block[k]) for k in block])


def mine_block():
    last_block = blockchain[-1]
    last_block_hash = hash_block(last_block)
    # print(f"Last block hash: {last_block_hash}")
    new_block = {
        "previous_hash": last_block_hash,
        "index": len(blockchain),
        "transactions": open_transactions,
    }
    blockchain.append(new_block)


def print_blockchain_elements():
    output = ""
    # output = ", ".join(map(str, blockchain))
    # output += "\n" + ("-" * 20)
    for block in blockchain:
        output += f"\n{block}"
    print(output)


def verify_chain():
    for i, block in enumerate(blockchain):
        if i > 0:
            if block["previous_hash"] != hash_block(blockchain[i - 1]):
                return False
    return True


def main():
    wait_for_input = True

    while wait_for_input:
        print("Choose Option:")
        print("  a: Add transaction amount")
        print("  m: Mine block")
        print("  p: Print chain")
        print("  h: Hack chain")
        print("  q: Quit")
        choice = get_user_choice()
        if choice == "a":
            recipient, sender, amount = get_transaction()
            add_transaction(recipient, sender, amount)
            print(open_transactions)
        elif choice == "m":
            mine_block()
        elif choice == "p":
            print_blockchain_elements()
        elif choice == "h":
            if len(blockchain) >= 1:
                blockchain[0]["transactions"] = [-1]
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
