const prompt = require("prompt-sync")({ sigint: true });

function log(m) { console.log(m) }

const bcTest = [
    [],
    [[], 1]
]
const bcTest2 = [
    [],
    [[], 1],
    [[[], 1], 2],
    [[[[], 1], 2], 3],
    [[[[[], 1], 2], 3], 4],
];

const genesisTransaction = {'prevHash': '', 'index': 0, 'transaction': {}}
const blockchain = [genesisTransaction];
const owner = 'Mak';

function getChoice() {
    return prompt("Choice: ");
}

function getLastTransaction() {
    return blockchain[blockchain.length - 1];
}

function hashBlock(block) {
    return JSON.stringify(block);
}


function addTransaction(sender, recipient, amount=1.0) {
    tx = {'sender': sender, 'recipient': recipient, 'amount': amount};
    newBlock = {'prevHash': hashBlock(getLastTransaction()), 'index': blockchain.length, 'transaction': tx}
    blockchain.push(newBlock);
}

function getUserInput() {
    sender = owner;
    recipient = prompt("Who is the recipient? ");
    amount = parseFloat(prompt("Your transaction amount please: "));
    return {'sender': sender, 'recipient': recipient, 'amount': amount};
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


function displayMenu() {
    log('Choose an option:');
    log('   a: Add transaction');
    log('   p: Print chain');
    log('   m: Manipulate');
    log('   q: Quit');
}

while (true) {
    displayMenu();
    const choice = getChoice();
    if (choice == 'a') {
        const txDetails = getUserInput()
        addTransaction(txDetails['sender'], txDetails['recipient'], txDetails['amount']);
    } else if (choice == 'p') {
        log(blockchain);
    } else if (choice == 'm') {
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
