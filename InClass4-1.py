import pygame
import math

t=0
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1400, 600))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def draw_player(position: pygame.Vector2, screen: pygame.Surface, *, color: pygame.Color, shape, size: int = 20):
    if shape == 'rect':
        rect = pygame.Rect(position, (size, size))
        pygame.draw.rect(screen, color, rect)

    elif shape == 'circle':
        pygame.draw.circle(screen, color, position, size)

    else:
        print("no shape specified")

def draw_obstacle(position: pygame.Vector2, screen: pygame.Surface):
    rect = pygame.Rect(position, (120, 10))
    pygame.draw.rect(screen, "white", rect)


t = 0
dt = 0.01

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 1
    if keys[pygame.K_DOWN]:
        player_pos.y += 1
    if keys[pygame.K_LEFT]:
        player_pos.x -= 1
    if keys[pygame.K_RIGHT]:
        player_pos.x += 1

    screen_width, screen_height = screen.get_size()
    player_pos.x = max(70, min(player_pos.x, screen_width - 100))
    player_pos.y = max(50, min(player_pos.y, screen_height - 120))

    draw_obstacle(player_pos + pygame.Vector2(-50,-30), screen)
    draw_player(player_pos + pygame.Vector2(-50, 0), screen, color="white", shape='rect', size=20)
    draw_player(player_pos + pygame.Vector2(50, 0), screen, color="white", shape='rect', size=20)
    draw_player(player_pos + pygame.Vector2(-30, 100 + 10 * math.sin(t/4)), screen, color="blue", shape='circle', size=10)
    draw_player(player_pos + pygame.Vector2(-10, 100), screen, color="red", shape='circle', size=10)
    draw_player(player_pos + pygame.Vector2(10, 100), screen, color="red", shape='circle', size=10)
    draw_player(player_pos + pygame.Vector2(30, 100), screen, color="red", shape='circle', size=10)
    draw_player(player_pos + pygame.Vector2(50, 100), screen, color="red", shape='circle', size=10)
    draw_player(player_pos + pygame.Vector2(70, 100 + 10 * math.sin(t/4)), screen, color="blue", shape='circle', size=10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60
    t += dt

pygame.quit()