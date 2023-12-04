import random
import math
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 400))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Figure:
    def __init__(self, color="Green", position=(200, 200)):
        self.color = color
        self.position = pygame.Vector2(position)

    def behave(self):
        pass

    def draw(self, screen: pygame.Surface):
        pass


class TriangleFigure(Figure):
    def __init__(self, color="Green", position=(200, 200), size=10):
        super().__init__(color, position)
        self.size = size
        self.rotation_angle = 0


    def behave(self):
        self.rotation_angle += 0.001


    def draw(self, screen: pygame.Surface):
        x1 = self.position.x + math.cos(self.rotation_angle) * self.size / 2
        y1 = self.position.y - self.size / 2 + math.sin(self.rotation_angle) * self.size / 2

        x2 = self.position.x - self.size / 2 - math.cos(self.rotation_angle) * self.size / 2
        y2 = self.position.y + self.size / 2 - math.sin(self.rotation_angle) * self.size / 2

        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 2)

        x2 = self.position.x + self.size / 2 - math.cos(self.rotation_angle) * self.size / 2
        y2 = self.position.y + self.size / 2 - math.sin(self.rotation_angle) * self.size / 2

        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 2)

        x1 = self.position.x - self.size / 2 - math.cos(self.rotation_angle) * self.size / 2
        y1 = self.position.y + self.size / 2 - math.sin(self.rotation_angle) * self.size / 2

        x2 = self.position.x + self.size / 2 - math.cos(self.rotation_angle) * self.size / 2
        y2 = self.position.y + self.size / 2 - math.sin(self.rotation_angle) * self.size / 2

        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 2)


class RectFigure(Figure):
    def __init__(self, color="Blue", position=(10, 20), width=50, height=60):
        super().__init__(color, position)
        self.width = width
        self.height = height
        self.position_bounce = 0

    def behave(self):
        self.position_bounce += 0.1

    def draw(self, screen: pygame.Surface):
        rect = pygame.Rect(self.position.x + math.sin(self.position_bounce) * 20, self.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect)

class CircleFigure(Figure):
    def __init__(self, color=("White"), position=(0, 0), size=40, increase_rate=0.2):
        super().__init__(color, position)
        self.size = size / 2
        self.increase_rate = increase_rate
        self.increase_size = 0

    def behave(self):
        self.increase_size += 0.2

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)),
                           self.size + math.sin(self.increase_size) * self.size / 2)

class StarFigure(Figure):
    def __init__(self, color="Yellow", position=(100, 100), size=20, num_points=5):
        super().__init__(color, position)
        self.size = size
        self.num_points = num_points
        self.rotation_angle = 0

    def behave(self):
        self.rotation_angle += 0.05

    def draw(self, screen: pygame.Surface):
        points = []
        for i in range(self.num_points * 2):
            angle = self.rotation_angle + math.pi * 2 * i / (self.num_points * 2)
            radius = self.size if i % 2 == 0 else self.size / 2
            x = self.position.x + math.cos(angle) * radius
            y = self.position.y + math.sin(angle) * radius
            points.append((x, y))
        pygame.draw.polygon(screen, self.color, points)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "white", "purple"]

figures = [
    TriangleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    RectFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    TriangleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    RectFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    TriangleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    RectFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), 50, 100),
    CircleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    CircleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    CircleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    CircleFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))),
    StarFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), size=random.randint(15, 30), num_points=5),
    StarFigure(random.choice(colors), (random.randint(0, screen.get_width()), random.randint(0, screen.get_height())), size=random.randint(15, 30), num_points=7)
]

def draw_scene_objects(screen: pygame.Surface):
    for figure in figures:
        figure.draw(screen)


def update_scene_objects():
    for figure in figures:
        figure.behave()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    update_scene_objects()
    draw_scene_objects(screen)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit()