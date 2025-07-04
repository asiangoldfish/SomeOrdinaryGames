import pygame
import numpy as np


class Button:
    def __init__(self, x, y, size_x, size_y, color: tuple):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size_x, self.size_y))

    ##########################################
    # Handlers
    ##########################################

    def on_hover(self):
        pass

    def on_press(self):
        pass

    def on_release(self):
        pass
