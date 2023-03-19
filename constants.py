import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH//COLUMNS

# rgb 
WHITE = (255, 252, 228)
BLACK = (133, 94, 66)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (45, 35))
