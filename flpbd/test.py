
import pygame

pygame.init()

screen = pygame.display.set_mode((80, 80))
pygame.display.set_caption('test')

a = pygame.image.load('iconka.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(a, (10, 10))
    pygame.display.flip()