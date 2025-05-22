import pygame
import numpy as np

class Sprite:
    def __init__(self, pos: np.ndarray, size: np.ndarray, color: np.ndarray):
        self.pos = pos
        self.size = size
        self.color = color
        self.rect = pygame.Rect((pos[0], pos[1], size[0], size[1]))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, tuple(self.color), self.rect)
        
    def set_position(self, new_pos: np.ndarray):
        self.rect.x = new_pos[0]
        self.rect.y = new_pos[1]
        self.pos = new_pos
    