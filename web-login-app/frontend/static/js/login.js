document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (validateForm(username, password)) {
            // Perform the login request
            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/dashboard'; // Redirect on success
                } else {
                    alert('Login failed. Please check your credentials.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again later.');
            });
        } else {
            alert('Please fill in both fields.');
        }
    });

    function validateForm(username, password) {
        return username.trim() !== '' && password.trim() !== '';
    }
});