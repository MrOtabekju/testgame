import pygame
import sys

# Pygame-ni ishga tushiramiz
pygame.init()

# O'yin o'lchami va oynani yaratamiz
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong o‘yini - ChatGPT versiyasi")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# O'yin elementlari
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
opponent = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)

# Harakat tezligi
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
opponent_speed = 5

# Ball o'yindan chiqsa hisob tiklanadi
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 50)

# FPS
clock = pygame.time.Clock()

# Funksiya: to'pni markazga qaytarish
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1
    ball_speed_y *= -1

# Asosiy o‘yin tsikli
while True:
    # Hodisalarni tekshirish
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tugmalar
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 6
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 6

    # Opponent harakati (oddiy AI)
    if opponent.centery < ball.centery:
        opponent.y += opponent_speed
    elif opponent.centery > ball.centery:
        opponent.y -= opponent_speed

    # To'p harakati
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ekran devorlariga urilishi
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Raketkaga urilishi
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Ball o'yindan chiqib ketganda
    if ball.left <= 0:
        player_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        opponent_score += 1
        reset_ball()

    # Ekranni tozalaymiz va chizamiz
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Hisobni chiqarish
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//2 + 20, 20))
    screen.blit(opponent_text, (WIDTH//2 - 40, 20))

    pygame.display.flip()
    clock.tick(60)
