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

const blockchain = [];


function getChoice() {
    return prompt("Choice: ");
}

function getLastTransaction() {
    if (blockchain.length < 1) {
        blockchain.push([0]);
    }
    return blockchain[blockchain.length - 1];
}

function addTransaction(transactionAmount, lastTransaction) {
    log("addValue(" + transactionAmount + ", " + lastTransaction + ")");
    blockchain.push([lastTransaction, transactionAmount]);
}

function getUserInput() {
    return parseFloat(prompt("Your transaction amount please: "));
}


function displayMenu() {
    log('Choose an option:');
    log('   a: Add transaction');
    log('   o: Output chain');
    log('   q: Quit');
}

while (true) {
    displayMenu();
    const choice = getChoice();
    if (choice == 'a') {
        addTransaction(getUserInput(), getLastTransaction());
    } else if (choice == 'o') {
        log(blockchain);
    } else {
        break;
    }

}
