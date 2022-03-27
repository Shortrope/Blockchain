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

const blockchain = [[]];



function getLastTransaction() {
    return blockchain[blockchain.length - 1];
}

function addValue(transactionAmount, lastTransaction) {
    log("addValue(" + transactionAmount + ", " + lastTransaction + ")");
    blockchain.push([lastTransaction, transactionAmount]);
}

function getUserInput() {
    return parseFloat(prompt("Your transaction amount please: "));
}



log(blockchain)
addValue(getUserInput(), getLastTransaction())
log(blockchain)
addValue(getUserInput(), getLastTransaction())
log(blockchain)
addValue(getUserInput(), getLastTransaction())
log(blockchain)
addValue(getUserInput(), getLastTransaction())
log(blockchain)