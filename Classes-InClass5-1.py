import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1200, 400))
clock = pygame.time.Clock()
running = True


class TriangleFigure:
    def __init__(self, color: int =(0, 255, 0), position=(0, 0), size: int =20):
        self.color = color
        self.position = pygame.Vector2(position)
        self.size = size
        self.rotation_angle = 0

    def behave(self):
        self.rotation_angle += 0.1
    def draw(self, screen: pygame.Surface):
        x1 = self.position.x + math.cos(self.rotation_angle) * self.size / 2
        y1 = self.position.y - self.size / 2 + math.sin(self.rotation_angle) * self.size / 2

        x2 = self.position.x - self.size / 2 + math.sin(self.rotation_angle) * self.size / 4
        y2 = self.position.y + self.size / 2

        x3 = self.position.x + self.size / 2
        y3 = self.position.y + self.size / 2 + math.sin(self.rotation_angle) * self.size / 2

        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 2)
        pygame.draw.line(screen, self.color, (x2, y2), (x3, y3), 2)
        pygame.draw.line(screen, self.color, (x3, y3), (x1, y1), 2)

class CircleFigure:
    def __init__(self, color=(0, 255, 0), position=(0, 0), size=10, increase_rate=0.2):
        self.color = color
        self.position = pygame.Vector2(position)
        self.size = size / 2
        self.increase_rate = increase_rate
        self.increase_size = 0

    def behave(self):
        self.increase_size += self.increase_rate

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)),
                           self.size + math.sin(self.increase_size) * self.size / 2)

class SquareFigure:
    def __init__(self, color=(255, 255, 0), position=(0, 0), size=20, increase_rate=0.2):
        self.color = color
        self.position = pygame.Vector2(position)
        self.size = size
        self.increase_rate = increase_rate
        self.increase_size = 0

    def behave(self):
        self.increase_size += self.increase_rate

    def draw(self, screen: pygame.Surface):
        half_size = self.size / 2
        dynamic_size = half_size + math.sin(self.increase_size) * half_size
        pygame.draw.rect(screen, self.color, (self.position.x - dynamic_size, self.position.y - dynamic_size, 2 * dynamic_size, 2 * dynamic_size), 2)


triangle_list = []
circle_list = []
square_list = []

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 105, 180), (255, 0, 255), (0, 255, 255)]

#triangle
for _ in range(100):
    color = random.choice(colors)
    x = random.randint(0, screen.get_width())
    y = random.randint(0, screen.get_height())

    size = random.randint(10, 50)
    triangle = TriangleFigure(color=color, position=pygame.Vector2(x, y), size=size)
    triangle_list.append(triangle)

#circle
for _ in range(50):
    color = random.choice(colors)
    x = random.randint(0, screen.get_width())
    y = random.randint(0, screen.get_height())

    size = random.randint(10, 50)
    increase_rate = random.uniform(0.1, 0.5)
    circle = CircleFigure(color=color, position=pygame.Vector2(x, y), size=size, increase_rate=increase_rate)
    circle_list.append(circle)

for _ in range(50):
    color = random.choice(colors)
    x = random.randint(0, screen.get_width())
    y = random.randint(0, screen.get_height())

    size = random.randint(20, 30)
    increase_rate = random.uniform(0.2, 0.3)
    square = SquareFigure(color=color, position=pygame.Vector2(x, y), size=size, increase_rate=increase_rate)
    square_list.append(square)

def update_scene_objects():
    #triangle
    for triangle in triangle_list:
        triangle.behave()

    for circle in circle_list:
        circle.behave()

    for square in square_list:
        square.behave()

def draw_scene_objects(screen: pygame.Surface):
    #triangle
    for triangle in triangle_list:
        triangle.draw(screen)
    #circle
    for circle in circle_list:
        circle.draw(screen)

    for square in square_list:
        square.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    update_scene_objects()
    draw_scene_objects(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
