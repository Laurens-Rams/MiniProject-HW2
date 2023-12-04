import pygame

# initialize pygame and screen
pygame.init()
screen = pygame.display.set_mode((1200, 400))

# load the image and convert to numpy array
img = pygame.image.load('data/test_cut.png').convert_alpha()
arr = pygame.surfarray.array3d(img)

# print the shape of the array
print(arr.shape)

# print couple of pixels to understand the structure
print(arr[2][0])
print(arr[3][0])
print(arr[4][0])

# convert to grayscale using for loops
for i in range(0, 16): # column number from 0 to 15
    for j in range(0, 16): # row number from 0 to 15
        r, g, b = arr[i][j] # get rgb values for the pixel
        avg = r/3  + g/3  + b/3 # calculate average
        arr[i][j] = [avg, avg, avg] # set rgb values to average

surface = pygame.surfarray.make_surface(arr) # convert array back to pygame surface
pygame.image.save(surface, 'data/test_gray.png') # save the surface as png