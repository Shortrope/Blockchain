const prompt = require("prompt-sync")({ sigint: true });

function log(m) { console.log(m) }

const MINING_REWARD = 10
const GENESIS_TRANSACTION = {'prevHash': '', 'index': 0, 'transactions': []}
const blockchain = [GENESIS_TRANSACTION];
const openTransactions = [];
const participants = new Set();
const owner = 'Mak';

function getChoice() {
    return prompt("Choice: ");
}

function getUserInput() {
    sender = owner;
    recipient = prompt("Who is the recipient? ");
    amount = parseFloat(prompt("Your transaction amount please: "));
    return {'sender': sender, 'recipient': recipient, 'amount': amount};
}

function getLastTransaction() {
    return blockchain[blockchain.length - 1];
}

function hashBlock(block) {
    return JSON.stringify(block);
}

function verifyTransaction(transaction) {
    let senderBalance = calcBalance(transaction['sender']);
    log(`verifyTransaction(): senderBalance ${senderBalance} : txAmount ${transaction['amount']}`);
    return senderBalance >= transaction['amount'];
}

function addTransaction(sender, recipient, amount=1.0) {
    let tx = {'sender': sender, 'recipient': recipient, 'amount': amount};
    if (verifyTransaction(tx)) {
        openTransactions.push(tx);
        participants.add(sender);
        participants.add(recipient);
        return true
    }
    return false
}

function mineBlock() {
    let rewardTx = {'sender': 'MINING', 'recipient': owner, 'amount': MINING_REWARD};
    openTransactions.push(rewardTx);
    let newBlock = {'prevHash': hashBlock(getLastTransaction()), 
                    'index': blockchain.length, 
                    'transactions': JSON.parse(JSON.stringify(openTransactions))};
    blockchain.push(newBlock);
    openTransactions.length = 0;
}

function verifyChain() {
    if (blockchain.length < 2) { return true; }
    for (index in blockchain) {
        if (index == 0) { continue; }
        if (blockchain[index]['prevHash'] != JSON.stringify(blockchain[index - 1])) {
            return false;
        }
    }
    return true;
}

function calcOpenTransactionsToBeSent(participant) {
    let sendAmount = 0;
    openTransactions.forEach(tx => {
        if (tx['sender'] == participant) {
            sendAmount += tx['amount'];
        }
    });
    return sendAmount
}

function calcBalance(participant) {
    let total = -(calcOpenTransactionsToBeSent(participant));
    blockchain.forEach(elem => {
        let transactions = elem['transactions'];
        transactions.forEach(tx => {
            if (tx['sender'] == participant) {
                total -= tx['amount'];
            }
            if (tx['recipient'] == participant) {
                total += tx['amount'];
            }
        });
    });
    return total;
}



function displayMenu() {
    log('Choose an option:');
    log('   a: Add transaction');
    log('   p: Print chain');
    log('   o: Print openTransactions');
    log('  pp: Print participants');
    log('   m: Mine blocks');
    log('   c: Calc Balances');
    log('   h: Hack');
    log('   t: Run Test Func');
    log('   q: Quit');
}

while (true) {
    displayMenu();
    const choice = getChoice();
    if (choice == 'a') {
        const txDetails = getUserInput()
        if (! addTransaction(txDetails['sender'], txDetails['recipient'], txDetails['amount'])) {
            log('Transaction failed: Insufficient funds!')
        };
    } else if (choice == 'p') {
        log(blockchain);
    } else if (choice == 'o') {
        log(openTransactions);
    } else if (choice == 'pp') {
        log('Participants:')
        participants.forEach(elem => {log(`  - ${elem}`)})
    } else if (choice == 'm') {
        mineBlock();
    } else if (choice == 'c') {
        participants.forEach(p => {log(`${p}: ${calcBalance(p)}`)})
    } else if (choice == 'h') {
        blockchain[0] = -1;
    } else if (choice == 'q') {
        break;
    } else {
        continue;
    }

    if (!verifyChain()) {
        log('INVALID BLOCKCHAIN!!!');
        log('Done!');
        log(blockchain);
        break;
    }

}
