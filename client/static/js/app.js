const apiUrl = 'http://localhost:5000';

async function fetchBlockchain() {
    const response = await fetch(`${apiUrl}/blockchain`);
    const data = await response.json();
    displayBlockchain(data);
}

function displayBlockchain(data) {
    const blockchainContainer = document.getElementById('blockchain');
    blockchainContainer.innerHTML = '';

    data.chain.forEach((block, index) => {
        const blockElement = document.createElement('div');
        blockElement.classList.add('block');
        blockElement.innerHTML = `
            <h3>Block ${index}</h3>
            <p>Hash: ${block.hash}</p>
            <p>Previous Hash: ${block.previousHash}</p>
            <p>Transactions: ${JSON.stringify(block.transactions)}</p>
            <p>Timestamp: ${new Date(block.timestamp).toLocaleString()}</p>
        `;
        blockchainContainer.appendChild(blockElement);
    });
}

async function createTransaction() {
    const transactionInput = document.getElementById('transactionInput').value;
    const response = await fetch(`${apiUrl}/transaction`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ transaction: transactionInput }),
    });

    if (response.ok) {
        fetchBlockchain();
        document.getElementById('transactionInput').value = '';
    } else {
        alert('Error creating transaction');
    }
}

document.getElementById('transactionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    createTransaction();
});

fetchBlockchain();