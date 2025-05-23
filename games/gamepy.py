import pygame
from time import sleep
from random import randint
from webbrowser import open

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('FLPBD')

f = pygame.font.SysFont(None, 100)

b_pos = 0
c_x = 500
c_y = randint(-450, -250)
grav = 0
spid = 7.0
count = 0

b_hitbox = pygame.Rect(120, b_pos, 15, 15)
c_hitbox1 = pygame.Rect(c_x, c_y, 80, 500)
c_hitbox2 = pygame.Rect(c_x, c_y + 600, 80, 500)

pygame.draw.circle(screen, 'red', (120, b_pos), 15)
count_display = f.render(str(count), True, 'green')


def draw_column(x, y):
    pygame.draw.rect(screen, 'white', (x, y, 80, 500))
    pygame.draw.rect(screen, 'white', (x, y + 600, 80, 500))


main_while = True
while main_while:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_while = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                grav = 13
    if b_pos > 400 or b_pos < 0:
        main_while = False
    if c_x < 5:
        c_x = 350
        c_y = randint(-450, -250)
        spid += 0.1
        count += 1
    if b_hitbox.colliderect(c_hitbox1) or b_hitbox.colliderect(c_hitbox2):
        main_while = False
        pygame.quit()
        open('https://fs.znanio.ru/methodology/images/70/e7/70e742b76806d6976095a3e3b87839aa855e0889.jpg')

    b_hitbox = pygame.Rect(120, b_pos, 15, 15)
    c_hitbox1 = pygame.Rect(c_x, c_y, 80, 500)
    c_hitbox2 = pygame.Rect(c_x, c_y + 600, 80, 500)

    screen.fill('black')
    draw_column(c_x, c_y)
    count_display = f.render(str(count), True, 'green')
    screen.blit(count_display, (20, 20))
    pygame.draw.circle(screen, 'red', (120, b_pos), 15)
    grav -= 2
    b_pos -= grav
    c_x -= spid
    sleep(0.05)
    print(f'grav={grav}, pos={b_pos}, col_y={c_y}')
    pygame.display.flip()
