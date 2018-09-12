import pygame


class Text:
    def __init__(self, surface, word, font, size, color, pos=(0,0), direction = "center"):
        self.surface = surface
        self.font = font
        self.size = size
        self.color = color
        self.word = word
        self.pos = pos
        self.direction = direction
        
    """method for define text object
        https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
        reference"""
    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.color)
        return textSurface, textSurface.get_rect()

    """Create method for write text on button"""
    def write(self):
        loadFont = pygame.font.SysFont("Courier New", self.size)
        textSurface, textRect = self.text_objects(self.word, loadFont)
        if self.direction == "center":
            textRect.center = (self.pos)
        elif self.direction == "left":
            textRect.left = (self.pos[0])
            textRect.top = (self.pos[1])
        elif self.direction == "right":
            textRect.right = (self.pos[0])
            textRect.top = (self.pos[1])
        self.surface.blit(textSurface, textRect)


