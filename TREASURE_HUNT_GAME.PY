

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 6
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10
NUM_TREASURES = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
RED = (220, 20, 60)
GREEN = (50, 205, 50)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌟 Treasure Hunt with Questions 🌟")

# Font
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 48, bold=True)

# Game clock
clock = pygame.time.Clock()

# Player start position
player_pos = [0, 0]

# Generate random treasure positions
def generate_treasures(num):
    treasures = []
    while len(treasures) < num:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if [x, y] != player_pos and [x, y] not in treasures:
            treasures.append([x, y])
    return treasures

treasures = generate_treasures(NUM_TREASURES)
score = 0

# Questions
questions = [
    {"question": "What is the capital of France?", "options": ["1. Berlin", "2. Paris", "3. Madrid", "4. Rome"], "answer": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"], "answer": 2},
    {"question": "What is 5 + 3?", "options": ["1. 6", "2. 7", "3. 8", "4. 9"], "answer": 3},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["1. Charles Dickens", "2. William Shakespeare", "3. Mark Twain", "4. J.K. Rowling"], "answer": 2},
    {"question": "Which is the largest mammal?", "options": ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus"], "answer": 2},
    {"question": "Which country is known as the Land of the Rising Sun?", "options": ["1. China", "2. Japan", "3. South Korea", "4. India"], "answer": 2},
    {"question": "What is the square root of 64?", "options": ["1. 6", "2. 7", "3. 8", "4. 9"], "answer": 3},
    {"question": "What is the chemical symbol for water?", "options": ["1. H2O", "2. CO2", "3. NaCl", "4. O2"], "answer": 1},
    {"question": "Who painted the Mona Lisa?", "options": ["1. Michelangelo", "2. Leonardo da Vinci", "3. Raphael", "4. Vincent van Gogh"], "answer": 2},
    {"question": "What is the tallest mountain in the world?", "options": ["1. Mount Everest", "2. K2", "3. Kangchenjunga", "4. Lhotse"], "answer": 1},
    {"question": "What is the capital of Germany?", "options": ["1. Berlin", "2. Paris", "3. Rome", "4. Madrid"], "answer": 1},
    {"question": "Which ocean is the largest?", "options": ["1. Atlantic", "2. Pacific", "3. Indian", "4. Arctic"], "answer": 2},
    {"question": "What is 12 x 12?", "options": ["1. 124", "2. 144", "3. 136", "4. 148"], "answer": 2},
    {"question": "Who discovered gravity?", "options": ["1. Galileo", "2. Newton", "3. Einstein", "4. Tesla"], "answer": 2},
    {"question": "What is the boiling point of water?", "options": ["1. 90°C", "2. 100°C", "3. 110°C", "4. 120°C"], "answer": 2},
]

# Draw grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

# Draw treasures
def draw_treasures():
    for tx, ty in treasures:
        pygame.draw.rect(screen, RED, (tx * CELL_SIZE, ty * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw player
def draw_player():
    px, py = player_pos
    pygame.draw.rect(screen, BLUE, (px * CELL_SIZE, py * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw info
def draw_info():
    text = font.render(f"Score: {score}/{NUM_TREASURES}", True, BLACK)
    screen.blit(text, (10, 10))

# Show instructions
def show_instructions():
    screen.fill(WHITE)
    instructions = [
        "Welcome to Treasure Hunt!",
        "Instructions:",
        "1. Use arrow keys to move.",
        "2. Reach the red blocks (treasures).",
        "3. Answer questions to collect treasures.",
        "Blue block: Your current position.",
        "Red blocks: Treasures.",
        "Collect all treasures to win!",
        "Press SPACE to start.",
    ]
    for i, line in enumerate(instructions):
        text = font.render(line, True, BLACK)
        screen.blit(text, (20, 20 + i * 30))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Ask MCQ question
def ask_question():
    question = random.choice(questions)
    screen.fill(WHITE)
    question_text = font.render(question["question"], True, BLACK)
    screen.blit(question_text, (10, 10))
    for i, option in enumerate(question["options"], start=1):
        option_text = font.render(option, True, BLACK)
        screen.blit(option_text, (10, 50 + i * 30))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and question["answer"] == 1:
                    return True
                elif event.key == pygame.K_2 and question["answer"] == 2:
                    return True
                elif event.key == pygame.K_3 and question["answer"] == 3:
                    return True
                elif event.key == pygame.K_4 and question["answer"] == 4:
                    return True
                else:
                    return False

# Main game loop
show_instructions()
running = True
while running:
    screen.fill(WHITE)

    draw_grid()
    draw_treasures()
    draw_player()
    draw_info()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            x, y = player_pos
            if event.key == pygame.K_UP and y > 0:
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and y < GRID_SIZE - 1:
                player_pos[1] += 1
            elif event.key == pygame.K_LEFT and x > 0:
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and x < GRID_SIZE - 1:
                player_pos[0] += 1

            # Collect treasure
            if player_pos in treasures:
                if ask_question():
                    treasures.remove(player_pos)
                    score += 1

    # Display feedback about player's position
    px, py = player_pos
    feedback = font.render(f"Player is at ({px}, {py}).", True, GREEN)
    screen.blit(feedback, (10, HEIGHT - 30))

    if not treasures:
        screen.fill(WHITE)
        win_message = big_font.render("🎉 You found all treasures! 🎉", True, GREEN)
        screen.blit(win_message, (WIDTH // 2 - win_message.get_width() // 2, HEIGHT // 2 - win_message.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


