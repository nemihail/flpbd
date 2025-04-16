import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('FLPBD')
pygame.display.set_icon(pygame.image.load('iconka.png'))

b_pos = 200
grav = 0

pygame.draw.circle(screen, 'red', (100, b_pos), 15)

main_while = True
while main_while:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_while = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grav -= 50
    if b_pos > 400 or b_pos < 0:
        main_while = False

    screen.fill('black')
    pygame.draw.circle(screen, 'red', (100, b_pos), 15)
    grav += 10
    b_pos = grav
    time.sleep(0.05)
    print(f'grav={grav}, pos={b_pos}')
    pygame.display.flip()
