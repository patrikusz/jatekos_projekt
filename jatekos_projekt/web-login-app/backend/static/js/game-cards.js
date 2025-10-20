// Game cards functionality
document.addEventListener('DOMContentLoaded', function() {
    // Toggle game description
    const toggleButtons = document.querySelectorAll('.game-description-toggle');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.stopPropagation();
            const description = this.nextElementSibling;
            
            if (description.classList.contains('active')) {
                description.classList.remove('active');
                this.textContent = 'Részletek ▼';
            } else {
                description.classList.add('active');
                this.textContent = 'Bezárás ▲';
            }
        });
    });
    
    // Optional: Click on card to play game (you can customize this)
    const gameCards = document.querySelectorAll('.game-card');
    
    gameCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't trigger if clicking the toggle button
            if (!e.target.classList.contains('game-description-toggle')) {
                const gameName = this.querySelector('.game-title').textContent;
                // Here you can add logic to start the game
                console.log('Starting game:', gameName);
                // For now, just show an alert
                // alert('Starting: ' + gameName);
            }
        });
    });
});
