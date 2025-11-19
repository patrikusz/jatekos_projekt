import tkinter as tk
import random
from flask import Flask, render_template

class SnakeGame:
    def __init__(self, root, width=400, height=400, delay=100):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=width, height=height, bg="black")
        self.canvas.pack()
        self.root.bind("<Key>", self.on_key_press)

        self.width = width
        self.height = height
        self.delay = delay

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"

        self.food = self.create_food()

        self.score = 0
        self.high_score = 0

        self.game_over = False
        self.update()

    def on_key_press(self, event):
        key = event.keysym
        directions = ["Up", "Down", "Left", "Right"]

        if key in directions:
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if key != opposite_directions[self.direction]:
                self.direction = key

    def create_food(self):
        x = random.randint(1, (self.width - 10) // 10) * 10
        y = random.randint(1, (self.height - 10) // 10) * 10
        return x, y

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="white", tags="snake")

    def draw_food(self):
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", tags="food")

    def draw_score(self):
        self.canvas.delete("score")
        self.canvas.create_text(
            50,
            10,
            text=f"Score: {self.score}   High Score: {self.high_score}",
            fill="white",
            anchor="nw",
            font=("Helvetica", 10),
            tags="score",
        )

    def check_collision(self):
        head = self.snake[0]
        if (
            head[0] < 0
            or head[0] >= self.width
            or head[1] < 0
            or head[1] >= self.height
            or head in self.snake[1:]
        ):
            self.game_over = True

    def update(self):
        if not self.game_over:
            self.move()
            self.check_collision()
            self.check_food_collision()
            self.draw_snake()
            self.draw_food()
            self.draw_score()
            self.root.after(self.delay, self.update)
        else:
            self.canvas.create_text(
                self.width // 2,
                self.height // 2,
                text=f"Game Over\nYour Score: {self.score}\nClick to Restart",
                fill="white",
                font=("Helvetica", 16),
                tags="game_over",
            )
            self.update_high_score()
            self.canvas.bind("<Button-1>", self.restart)

    def move(self):
        head = list(self.snake[0])
        if self.direction == "Up":
            head[1] -= 10
        elif self.direction == "Down":
            head[1] += 10
        elif self.direction == "Left":
            head[0] -= 10
        elif self.direction == "Right":
            head[0] += 10
        self.snake = [tuple(head)] + self.snake[:-1]

    def check_food_collision(self):
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.canvas.delete("food")  # Remove the food from the canvas
            self.food = self.create_food()
            self.draw_food()  # Draw the new food
            self.score += 10

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def restart(self, event):
        self.canvas.delete("food")  # Remove all food from the canvas
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.game_over = False
        self.canvas.delete("game_over")
        self.update()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
