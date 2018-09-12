import pygame

class Button:

    def __init__(self, mouse, surf, text='button', wdborder = 2, color=(51, 51, 51), pos=(0, 0, 70, 80)):
        self.color = color
        self.mouse = mouse
        self.surf = surf
        self.text = text
        self.pos = pos
        self.wdborder = wdborder
        
    
    def textSet(self, text):
        self.text = text
    def colorSet(self, color):
        self.color = color
    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.pos, self.wdborder)
        