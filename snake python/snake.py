import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
FPS = 10
SNAKE_SIZE = 10  # Tamanho do segmento da cobra

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inicialização da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

# Fontes
font_big = pygame.font.Font(None, 72)
font_small = pygame.font.Font(None, 36)

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Função para desenhar a cobra
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, SNAKE_SIZE, SNAKE_SIZE))

# Função para desenhar a maçã
def draw_apple(apple):
    pygame.draw.rect(screen, RED, (*apple, SNAKE_SIZE, SNAKE_SIZE))

# Função para mostrar texto na tela
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Função para desenhar o menu
def draw_menu():
    screen.fill(BLACK)
    draw_text("Jogo da Cobrinha", font_big, GREEN, WIDTH // 2, HEIGHT // 4)
    draw_text("Começar", font_small, GREEN, WIDTH // 2, HEIGHT // 2)
    draw_text("Sair", font_small, GREEN, WIDTH // 2, HEIGHT // 2 + 50)
    pygame.display.flip()

# Função para iniciar o jogo
def start_game():
    snake_game()

# Função principal do jogo
def snake_game():
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = RIGHT
    apple = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
             random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
    score = 0
    speed = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != DOWN:
            direction = UP
        elif keys[pygame.K_DOWN] and direction != UP:
            direction = DOWN
        elif keys[pygame.K_LEFT] and direction != RIGHT:
            direction = LEFT
        elif keys[pygame.K_RIGHT] and direction != LEFT:
            direction = RIGHT

        # Atualizar a posição da cobra
        x, y = snake[0]
        x += direction[0] * SNAKE_SIZE
        y += direction[1] * SNAKE_SIZE
        snake.insert(0, (x, y))

        # Verificar colisão com a maçã
        if snake[0] == apple:
            apple = (random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                     random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
            score += 1
            speed += 1
        else:
            snake.pop()

        # Verificar colisão com as bordas
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            return "game_over", score

        # Verificar colisão com a própria cobra
        if len(snake) != len(set(snake)):
            return "game_over", score

        # Limpar a tela
        screen.fill(BLACK)

        # Desenhar a maçã
        draw_apple(apple)

        # Desenhar a cobra
        draw_snake(snake)

        # Desenhar pontuação
        draw_text(f"Pontuação: {score}", font_small, GREEN, WIDTH // 2, 20)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de frames por segundo
        clock.tick(speed)

# Função para exibir a tela de Game Over
def game_over_screen(score):
    while True:
        screen.fill(BLACK)
        draw_text("Game Over", font_big, RED, WIDTH // 2, HEIGHT // 4)
        draw_text(f"Pontuação: {score}", font_small, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Reiniciar", font_small, GREEN, WIDTH // 2, HEIGHT // 2 + 50)
        draw_text("Sair", font_small, GREEN, WIDTH // 2, HEIGHT // 2 + 100)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH // 2 - 50 < mouse_pos[0] < WIDTH // 2 + 50 and HEIGHT // 2 + 25 < mouse_pos[1] < HEIGHT // 2 + 75:
                    return "restart"
                elif WIDTH // 2 - 50 < mouse_pos[0] < WIDTH // 2 + 50 and HEIGHT // 2 + 75 < mouse_pos[1] < HEIGHT // 2 + 125:
                    return "menu"

# Função principal
def main():
    in_menu = True

    while in_menu:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if WIDTH // 2 - 50 < mouse_pos[0] < WIDTH // 2 + 50 and HEIGHT // 2 - 25 < mouse_pos[1] < HEIGHT // 2 + 25:
                    result = snake_game()
                    while result[0] == "game_over":
                        result = game_over_screen(result[1])
                        if result == "restart":
                            result = snake_game()  # Continuar reiniciando o jogo
                        elif result == "menu":
                            break
                elif WIDTH // 2 - 50 < mouse_pos[0] < WIDTH // 2 + 50 and HEIGHT // 2 + 25 < mouse_pos[1] < HEIGHT // 2 + 75:
                    pygame.quit()
                    sys.exit()

# Chamada para a função principal
if __name__ == "__main__":
    main()
