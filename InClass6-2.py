import pygame
class Filter():
    def __init__(self, image_src):
        self.image_src = image_src
        self.img = None
        self.arr = None

    def load_image(self):
        self.img = pygame.image.load(self.image_src).convert_alpha()
        self.arr = pygame.surfarray.array3d(self.img)

    def save_image(self, save_path):
        surface = pygame.surfarray.make_surface(self.arr)
        pygame.image.save(surface, save_path)

    def transformer(self):
        pass

class GrayScaleFilter(Filter):
    def transform(self):
        for i in range(0, 16):  # column number from 0 to 15
            for j in range(0, 16):  # row number from 0 to 15
                r, g, b = self.arr[i][j]  # get rgb values for the pixel
                avg = r / 3 + g / 3 + b / 3  # calculate average
                self.arr[i][j] = [avg, avg, avg]  # set rgb values to average

class FunnyFilter(Filter):
    def transform(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.arr[i][j] = [255 - self.arr[i][j][0], 255 - self.arr[i][j][1], 255 - self.arr[i][j][2]]


pygame.init()
screen = pygame.display.set_mode((1200, 400))

image_file = "data/test_cut.png"
gray_filter = GrayScaleFilter(image_file)
funny_filter = FunnyFilter(image_file)

gray_filter.load_image()
gray_filter.transform()
gray_filter.save_image("data/test_gray.png")

funny_filter.load_image()
funny_filter.transform()
funny_filter.save_image("data/test_funny.png")
