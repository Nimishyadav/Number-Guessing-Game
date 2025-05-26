import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
FONT = pygame.font.SysFont("Arial", 28)
SMALL_FONT = pygame.font.SysFont("Arial", 22)

# Input box
input_box = pygame.Rect(150, 150, 200, 40)
button_rect = pygame.Rect(180, 310, 140, 40)

# Game variables
def reset_game():
    global secret_number, guess, feedback, attempts, game_over, won
    secret_number = random.randint(1, 100)
    guess = ''
    feedback = "Guess a number between 1 and 100"
    attempts = 0
    game_over = False
    won = False

reset_game()

def draw():
    screen.fill(WHITE)
    title = FONT.render("Number Guessing Game", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    pygame.draw.rect(screen, GRAY, input_box)
    guess_text = FONT.render(guess, True, BLACK)
    screen.blit(guess_text, (input_box.x + 10, input_box.y + 5))

    feedback_color = GREEN if won else (RED if game_over else BLACK)
    feedback_text = SMALL_FONT.render(feedback, True, feedback_color)
    screen.blit(feedback_text, (WIDTH // 2 - feedback_text.get_width() // 2, 220))

    attempts_text = SMALL_FONT.render(f"Attempts: {attempts}/10", True, BLACK)
    screen.blit(attempts_text, (WIDTH // 2 - attempts_text.get_width() // 2, 260))

    if game_over:
        pygame.draw.rect(screen, GRAY, button_rect)
        button_text = SMALL_FONT.render("Play Again", True, BLACK)
        screen.blit(button_text, (button_rect.x + 20, button_rect.y + 8))

    pygame.display.flip()

# Main loop
running = True
while running:
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect.collidepoint(event.pos):
                reset_game()

        if not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if guess.isdigit():
                    number = int(guess)
                    if 1 <= number <= 100:
                        attempts += 1
                        if number < secret_number:
                            feedback = "Too low!"
                        elif number > secret_number:
                            feedback = "Too high!"
                        else:
                            feedback = f"🎉 Correct! It was {secret_number}"
                            won = True
                            game_over = True
                        if attempts >= 10 and not won:
                            feedback = f"💀 Game Over! It was {secret_number}"
                            game_over = True
                    else:
                        feedback = "Enter a number between 1 and 100"
                else:
                    feedback = "Please enter a valid number"
                guess = ''
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            elif event.unicode.isdigit() and len(guess) < 3:
                guess += event.unicode

pygame.quit()
sys.exit()
