// script.js
const buttons = document.querySelectorAll('button');
const resultElement = document.getElementById('result');

buttons.forEach(button => {
    button.addEventListener('click', async () => {
        const userChoice = button.id;

        try {
            const response = await fetch('http://127.0.0.1:8080/play', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_choice: userChoice }),
            });

            if (response.ok) {
                const data = await response.json();
                resultElement.textContent = `You chose ${userChoice}. Computer chose ${data.result}. Result: ${data.result}`;
            } else {
                console.error('Error fetching data:', response.status);
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
});
