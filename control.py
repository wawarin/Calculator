import pygame
from Button import *
from Text import *


class Controller:
    def __init__(self):
        pygame.init()
        self.running = True 
        self.width, self.height = 400, 600 # difine width, height
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption('Calculator')
        self.mouse = 0, 0 #set default of mouse position 
        self.color = ((249, 216, 104), (244, 240, 122), (248, 252, 126), (238, 230, 133))# color backgrond of button
        

    """method set mouse"""
    def mousePos(self, mouse):
        self.mouse = mouse
    
    """method get value mouse"""
    def getmousePos(self):
        return self.mouse
    
    # def cal(self, eq):
    #     result = "".join(eq)
    #     result = str(eval(result))
    #     eq = result

    """method for run program"""
    def run(self):
        key = []
        row = 5 # row of button
        col = 4 # column of button
        space = 3
        symbol = (("C","()","%","÷"),("7","8","9","x"),("4","5","6","-"),("1","2","3","+"),("+/-","0",".","=")) # text on button keep it in tuple
        self.gameDisplay.fill((230, 230, 250))

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False            

            self.mousePos(pygame.mouse.get_pos())# get mouse position

            """Draw rectangle for backgound of button"""
            pygame.draw.rect(self.gameDisplay, self.color[0], (((self.width / 4) * 0), self.height / 3, self.width / 4, self.height - (self.height / 3)))
            pygame.draw.rect(self.gameDisplay, self.color[1], (((self.width / 4) * 1), self.height / 3, self.width / 4, self.height - (self.height / 3)))
            pygame.draw.rect(self.gameDisplay, self.color[2], (((self.width / 4) * 2), self.height / 3, self.width / 4, self.height - (self.height / 3)))
            pygame.draw.rect(self.gameDisplay, self.color[3], (((self.width / 4) * 3), self.height / 3, self.width / 4, self.height - (self.height / 3)))

            """Loop for row and column"""
            for i in range(row):
                for j in range(col):

                    """set variable for short coding"""
                    button_width = self.width / col - 2 * space # 
                    button_height = 2 * self.height / 15 - 2 * space
                    xpos = space + (button_width + 2 * space) * j
                    ypos = self.height / 3 + space + (button_height + 2 * space) * i
                    
                    """Codition for check position in column and row of button"""
                    if (xpos <= self.getmousePos()[0] <= xpos + button_width) and (ypos <= self.getmousePos()[1] <= ypos + button_height):
                        button = Button(self.mouse, self.gameDisplay, color=(254, 119, 125), pos = (xpos, ypos, button_width, button_height), wdborder = 0)
                        button.draw()

                        """Codition for check click mouse on button"""
                        if pygame.mouse.get_pressed()[0]:

                            for k in pygame.event.get():
                                bracket = 0
                                posneg = 0
                                showdis = "".join(key)

                                """Condition for show equation display"""
                                if key == []:
                                    pygame.draw.rect(self.gameDisplay, (230, 230, 250), (0, 0, self.width, self.height / 3))
                                    txt = Text(self.gameDisplay, "0", "Courier New", 60, (51, 51, 51), (self.width, (self.height / 3) / 3 ), "right").write()
                                elif key != []:
                                    pygame.draw.rect(self.gameDisplay, (230, 230, 250), (0, 0, self.width, self.height / 3))
                                    txt = Text(self.gameDisplay, showdis, "Courier New", 60, (51, 51, 51), (self.width, (self.height / 3) / 3 ), "right").write()

                                """Condition for check position on your click"""
                                if k.type == pygame.MOUSEBUTTONUP:
                                    print(self.getmousePos())
                                    if i == 0:
                                        if j == 0:
                                            key.append("Clear")
                                        elif j == 1:
                                            if bracket == 0:
                                                key.append("(")
                                                bracket = 1
                                            elif bracket == 1:
                                                key.append(")")
                                                bracket = 0
                                        elif j == 2:
                                            key.append("%")
                                        elif j == 3:
                                            key.append("/")
                                    elif i == 1:
                                        if j == 0:
                                            key.append("7")
                                        elif j == 1:
                                            key.append("8")
                                        elif j == 2:
                                            key.append("9")
                                        elif j == 3:
                                            key.append("*")
                                    elif i == 2:
                                        if j == 0:
                                            key.append("4")
                                        elif j == 1:
                                            key.append("5")
                                        elif j == 2:
                                            key.append("6")
                                        elif j == 3:
                                            key.append("-")
                                    elif i == 3:
                                        if j == 0:
                                            key.append("1")
                                        elif j == 1:
                                            key.append("2")
                                        elif j == 2:
                                            key.append("3")
                                        elif j == 3:
                                            key.append("+")
                                    elif i == 4:
                                        if j == 0:
                                            if posneg == 0:
                                                key.append("(-")
                                                posneg = 1
                                            elif posneg == 1:
                                                key.append("")
                                                posneg == 0
                                        elif j == 1:
                                            key.append("0")
                                        elif j == 2:
                                            key.append(".")
                                        elif j == 3:
                                            print(key)
                                            show = "".join(key)
                                            show = str(eval(show)) # calculator of equation
                                            key = list(show)

                                    print(key)
                                               
                    else:
                        button = Button(self.mouse, self.gameDisplay, color=(229, 186, 250), pos = (xpos, ypos, button_width, button_height), wdborder = 0)
                        button.draw()

                    """Draw text on button"""
                    txt = Text(self.gameDisplay, symbol[i][j], "Courier New", 50, (51, 51, 51), ((xpos + button_width / 2), (ypos + button_height / 2))).write()
                    # txt = Text(self.gameDisplay, "0", "Courier New", 60, (51, 51, 51), (self.width, (self.height / 3) / 3 ), "right").write()
            pygame.display.update()
        pygame.quit()
        quit()
   
app = Controller()
app.run()
