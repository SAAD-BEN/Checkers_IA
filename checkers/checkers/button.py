import pygame
from checkers.constants import BUTTON_DIMENSIONS, BUTTON_DEFAULT_FONT, BUTTON_FONT_COLORS, PADDING, GAME_OVER_FONT_SMALL, RED

class Button:
    def __init__(self, button_id, text, x, y, color, type):
        self.button_id = button_id
        self.text = text
        self.x = x
        self.y = y
        self.width = BUTTON_DIMENSIONS[type][0]
        self.height = BUTTON_DIMENSIONS[type][1]
        self.color = color
        self.font = BUTTON_DEFAULT_FONT[type]
        self.font_color = BUTTON_FONT_COLORS[type]
        self.centered_text = (type != 2)  # type 2 buttons are not centered

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height),border_radius= 15)
        text = self.font.render(self.text, 1, self.font_color)
        if self.centered_text:
            win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                            self.y + round(self.height / 2) - round(text.get_height() / 2)))
        else:
            win.blit(text, (self.x + PADDING, self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def drawEnd(self, win):
        text = GAME_OVER_FONT_SMALL.render(self.text, 1, RED)
        if self.centered_text:
            win.blit(text, (self.x - round(text.get_width() / 2),
                            self.y - round(text.get_height() / 2)))
        else:
            win.blit(text, (self.x - round(text.get_width() / 2),
                            self.y - round(text.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if (self.x <= x1 <= self.x + self.width
                and self.y <= y1 <= self.y + self.height):
            return True
        else:
            return False