import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 400))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class TriangleFigure:
    color: str = "Green"
    position: pygame.Vector2 = pygame.Vector2(0, 0)
    size: int = 20

    def draw(self, screen: pygame.Surface):
        x1 = self.position.x
        y1 = self.position.y - self.size / 2

        x2 = self.position.x - self.size / 2
        y2 = self.position.y + self.size / 2

        pygame.draw.line(screen, self.color, (x1, y1), (x2, y2), 2)

triangle_red = TriangleFigure()
triangle_blue = TriangleFigure()

triangle_red.color = "Red"
triangle_red.position = pygame.Vector2(100, 100)
triangle_red.size = 30

triangle_blue.color = "Blue"
triangle_blue.position = pygame.Vector2(200, 50)
triangle_blue.size = 20

def draw_scene_objects(screen: pygame.Surface):
    triangle_red.draw(screen)
    triangle_blue.draw(screen)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    draw_scene_objects(screen)

    pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60

pygame.quit()