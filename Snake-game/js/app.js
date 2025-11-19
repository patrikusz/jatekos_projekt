class Game {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.gridSize = 20;
        this.snake = [{ x: 100, y: 100 }];
        this.direction = 'right';
        this.food = this.createFood();
        this.score = 0;
        this.highScore = 0;
        this.gameRunning = true;

        this.drawSquare = this.drawSquare.bind(this);
        this.createFood = this.createFood.bind(this);
        this.draw = this.draw.bind(this);
        this.update = this.update.bind(this);
        this.collisionWithSelf = this.collisionWithSelf.bind(this);
        this.resetGame = this.resetGame.bind(this);

        document.addEventListener('keydown', this.handleKeyPress.bind(this));
        window.addEventListener('resize', this.handleWindowResize.bind(this));

        this.handleWindowResize();
        setInterval(this.update, 200);
    }

    createFood() {
        const x = Math.floor(Math.random() * (this.canvas.width / this.gridSize)) * this.gridSize;
        const y = Math.floor(Math.random() * (this.canvas.height / this.gridSize)) * this.gridSize;
        return { x, y };
    }

    drawSquare(x, y, color) {
        this.ctx.fillStyle = color;
        this.ctx.fillRect(x, y, this.gridSize, this.gridSize);  
    }

    drawCircle(x, y, radius, color) {
        this.ctx.fillStyle = color;
        this.ctx.beginPath();
        this.ctx.arc(x, y, radius, 0, 2 * Math.PI);
        this.ctx.fill();
    }

    draw() {
        // Clear the canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw the snake
        this.snake.forEach((segment, index) => {
            const color = index % 2 === 0 ? 'black' : 'orange';
            this.drawSquare(segment.x, segment.y, color);
        });

        // Draw the food as a circle
        const foodRadius = this.gridSize / 2;
        this.drawCircle(this.food.x + foodRadius, this.food.y + foodRadius, foodRadius, 'yellow');

        // Draw the score and high score
        this.ctx.fillStyle = 'white';
        this.ctx.font = '2rem Arial';
        this.ctx.fillText(`Score: ${this.score}   High Score: ${this.highScore}`, 20, 40);

        if (!this.gameRunning) {
            this.ctx.fillStyle = 'white';
            this.ctx.font = '4rem arial ';
            const gameOverText = 'Game Over! Press Enter to restart.';
            const textWidth = this.ctx.measureText(gameOverText).width;
            this.ctx.fillText(gameOverText, (this.canvas.width - textWidth) / 2, this.canvas.height / 2);
        }
    }

    update() {
        if (!this.gameRunning) {
            return;
        }

        // Move the snake
        const head = { ...this.snake[0] };
        switch (this.direction) {
            case 'up':
                head.y -= this.gridSize;
                break;
            case 'down':
                head.y += this.gridSize;
                break;
            case 'left':
                head.x -= this.gridSize;
                break;
            case 'right':
                head.x += this.gridSize;
                break;
        }
        this.snake.unshift(head);

        // Check for collision with food
        if (head.x === this.food.x && head.y === this.food.y) {
            this.score += 10;
            if (this.score > this.highScore) {
                this.highScore = this.score;
            }
            this.food = this.createFood();
        } else {
            // Remove the tail
            this.snake.pop();
        }

        // Check for collision with walls or itself
        if (
            head.x < 0 ||
            head.x >= this.canvas.width ||
            head.y < 0 ||
            head.y >= this.canvas.height ||
            this.collisionWithSelf()
        ) {
            this.gameRunning = false;
        }

        this.draw();
    }

    collisionWithSelf() {
        return this.snake.slice(1).some(segment => segment.x === this.snake[0].x && segment.y === this.snake[0].y);
    }

    resetGame() {
        this.snake = [{ x: 100, y: 100 }];
        this.direction = 'right';
        this.score = 0;
        this.food = this.createFood();
        this.gameRunning = true;
    }

    handleKeyPress(event) {
        // Prevent the browser from scrolling when arrow keys are pressed
        if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) {
            event.preventDefault();
        }

        switch (event.key) {
            case 'ArrowUp':
                this.direction = 'up';
                break;
            case 'ArrowDown':
                this.direction = 'down';
                break;
            case 'ArrowLeft':
                this.direction = 'left';
                break;
            case 'ArrowRight':
                this.direction = 'right';
                break;
            case 'Enter':
                this.resetGame();
                break;
        }
    }

    handleWindowResize() {
        this.canvas.width = window.innerWidth - 20; // Adjust as needed
        this.canvas.height = window.innerHeight - 20; // Adjust as needed
        this.food = this.createFood(); // Reset food position on window resize
        this.draw();
    }
}

const canvas = document.getElementById('gameCanvas');
const game = new Game(canvas);