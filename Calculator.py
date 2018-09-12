import pygame

pygame.init()
# size = (320, 500)
width = 200
height = 500
gameDisplay = pygame.display.set_mode((width, height))
screen = pygame.display.set_caption('Calculator')


class createButton:

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            print(event)
            pygame.display.update()
    pygame.quit()
    quit()

    def button(self):
        pygame.draw.rect(gameDisplay, (249, 216, 104), (80, 150, 80, 350), )
        pygame.draw.rect(gameDisplay, (244, 240, 122), (160, 150, 80, 350))
        pygame.draw.rect(gameDisplay, (248, 252, 126), (240, 150, 80, 350))
        pygame.draw.rect(gameDisplay, (242, 153, 101), (0, 150, 80, 350))

        mpos = pygame.mouse.get_pos()
        for i in range(1, width, 80):
            for j in range(151, height, 70):
                print(mpos[0], mpos[1])

                pygame.draw.rect(gameDisplay, (51, 51, 51), (i, j, 78, 68), 2)
                if (mpos[0] >= 0 and mpos[0] <= i + 80) and (mpos[1] >= 150 and mpos[1] <= j + 70):
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (i, j, 78, 68))

draw = createButton
draw.button()
