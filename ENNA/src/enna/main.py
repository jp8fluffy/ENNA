from typing import Text
import pygame

pygame.init()

# Create window
window = pygame.display.set_mode((500, 500))

# Title window
pygame.display.set_caption("ENNA")
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.display.update()
