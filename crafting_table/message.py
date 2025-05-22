import pygame

class Message:
    def __init__(self, pos, font_size=100, text="Hello world", color=(0,0,0)):
        self._text = text
        self.pos = pos
        self.color = color
        self.font = pygame.font.SysFont("Comic Sans MS", font_size)
        self.text_surface = self.font.render(self._text, False, self.color)

    def draw(self, screen):
        screen.blit(self.text_surface, self.pos)

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.text_surface = self.font.render(new_text, False, self.color)

