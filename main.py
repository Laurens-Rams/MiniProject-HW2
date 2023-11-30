
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Circle properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 10
dx, dy = 5, 3.5

# Trail effect
trail_length = 4000
trail = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    if x + radius > WIDTH or x - radius < 0:
        dx = -dx
    if y + radius > HEIGHT or y - radius < 0:
        dy = -dy

    trail.append((x, y, random_color()))
    if len(trail) > trail_length:
        trail.pop(0)

    for t in trail:
        pygame.draw.circle(screen, t[2], (t[0], t[1]), radius)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
