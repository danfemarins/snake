
// Variáveis do jogo
const canvas = document.getElementById("snakeCanvas");
const ctx = canvas.getContext("2d");
const snakeSize = 10;
let snake = [{ x: 100, y: 100 }, { x: 90, y: 100 }, { x: 80, y: 100 }];
let direction = "RIGHT";
let apple = { x: 200, y: 200 };
let score = 0;
let speed = 100;
let gameInterval;

function showMenu() {
    document.getElementById("menu").style.display = "block";
    document.getElementById("snakeCanvas").style.display = "none";
    document.getElementById("gameOver").style.display = "none";
}

function showGame() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("snakeCanvas").style.display = "block";
    document.getElementById("gameOver").style.display = "none";
    startGame();
}

function showGameOver() {
    document.getElementById("menu").style.display = "none";
    document.getElementById("snakeCanvas").style.display = "none";
    document.getElementById("gameOver").style.display = "block";
    document.getElementById("scoreText").innerText = "Pontuação: " + score;
}

function restartGame() {
    resetGame();
    showGame();
}

function exitGame() {
    showMenu();
}

function drawSnake() {
    ctx.fillStyle = "green";
    snake.forEach(segment => {
        ctx.fillRect(segment.x, segment.y, snakeSize, snakeSize);
    });
}

function drawApple() {
    ctx.fillStyle = "red";
    ctx.fillRect(apple.x, apple.y, snakeSize, snakeSize);
}

function drawScore() {
    ctx.fillStyle = "black";
    ctx.font = "20px Arial";
    ctx.fillText("Pontuação: " + score, 10, 20);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function checkCollision() {
    const head = snake[0];
    if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height) {
        gameOver();
    }

    for (let i = 1; i < snake.length; i++) {
        if (head.x === snake[i].x && head.y === snake[i].y) {
            gameOver();
        }
    }

    if (head.x === apple.x && head.y === apple.y) {
        eatApple();
    }
}

function gameOver() {
    clearInterval(gameInterval);
    alert("Game Over! Pontuação: " + score);
    resetGame();
    showMenu();
}

function resetGame() {
    snake = [{ x: 100, y: 100 }, { x: 90, y: 100 }, { x: 80, y: 100 }];
    direction = "RIGHT";
    apple = { x: 200, y: 200 };
    score = 0;
    speed = 100;
}

function eatApple() {
    score++;
    speed -= 5;
    const tail = { x: snake[snake.length - 1].x, y: snake[snake.length - 1].y };
    snake.push(tail);
    generateNewApple();
}

function generateNewApple() {
    const maxX = canvas.width / snakeSize;
    const maxY = canvas.height / snakeSize;
    apple = {
        x: Math.floor(Math.random() * maxX) * snakeSize,
        y: Math.floor(Math.random() * maxY) * snakeSize
    };
}

function updateGame() {
    const head = { x: snake[0].x, y: snake[0].y };

    if (direction === "RIGHT") head.x += snakeSize;
    if (direction === "LEFT") head.x -= snakeSize;
    if (direction === "UP") head.y -= snakeSize;
    if (direction === "DOWN") head.y += snakeSize;

    snake.unshift(head);
    snake.pop();
}

function drawGame() {
    clearCanvas();
    drawSnake();
    drawApple();
    drawScore();
    checkCollision();
    updateGame();
}

function startGame() {
    resetGame();
    gameInterval = setInterval(drawGame, speed);
}

window.onload = showMenu;

document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp" && direction !== "DOWN") direction = "UP";
    if (event.key === "ArrowDown" && direction !== "UP") direction = "DOWN";
    if (event.key === "ArrowLeft" && direction !== "RIGHT") direction = "LEFT";
    if (event.key === "ArrowRight" && direction !== "LEFT") direction = "RIGHT";
});
