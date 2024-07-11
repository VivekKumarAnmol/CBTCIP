// script.js
const buttons = document.querySelectorAll('button');
const resultElement = document.getElementById('result');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        const userChoice = button.id;
        const computerChoice = getRandomChoice();
        const result = determineWinner(userChoice, computerChoice);
        resultElement.textContent = `You chose ${userChoice}. Computer chose ${computerChoice}. Result: ${result}`;
    });
});

function getRandomChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    return choices[Math.floor(Math.random() * choices.length)];
}

function determineWinner(user, computer) {
    if (user === computer) return 'It\'s a tie!';
    if ((user === 'rock' && computer === 'scissors') ||
        (user === 'paper' && computer === 'rock') ||
        (user === 'scissors' && computer === 'paper')) {
        return 'You win!';
    } else {
        return 'Computer wins!';
    }
}
