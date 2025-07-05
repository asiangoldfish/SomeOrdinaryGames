import pygame


class BaseUI:
    def __init__(self):
        pass

    def handle_events(self, event):
        pass

    def draw(self, screen: pygame.Surface):
        pass
