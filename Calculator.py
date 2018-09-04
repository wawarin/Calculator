

import pygame
pygame.init()
# size = (320, 500)
width = 320
height = 500
gameDisplay = pygame.display.set_mode((width, height))
screen = pygame.display.set_caption('Calculator')

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        print(event)

    pygame.display.update()
    clock.tick(60)

    pygame.draw.rect(gameDisplay, (249, 216, 104), (80, 150, 80, 350),)
    pygame.draw.rect(gameDisplay, (244, 240, 122), (160, 150, 80, 350))
    pygame.draw.rect(gameDisplay, (248, 252, 126), (240, 150, 80, 350))
    pygame.draw.rect(gameDisplay, (242, 153, 101), (0, 150, 80, 350))

    for i in range(1, width, 80):
        for j in range(151, height, 70):

            pygame.draw.rect(gameDisplay, (51, 51, 51), (i, j, 78, 68), 2)

pygame.quit()
quit()

