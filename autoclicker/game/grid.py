import numpy as np
import pygame

import random
random.seed(5)


class Grid:
    def __init__(self, pos, size, rows, color, gap, items):
        if size.size != 2:
            print("Size must be 2")
        elif size[0] < 1:
            print("There must be at least 1 horizontal tile(s)")
        elif size[1] < 1:
            print("There must be at least 1 vertical tile(s)")

        self.pos = pos
        self.size = size
        self.rows = rows
        self.colors = np.full((rows, 4), color, dtype=np.uint8)

        self.tiles = list()
        self._gap = gap + size
        self.positions = list()

        self.highlight_color = pygame.Color("yellow")
        self.default_color = pygame.Color(70, 30, 50)

        self.items = items

    @property
    def gap(self):
        return self._gap

    @gap.setter
    def gap(self, new_gap):
        self._gap = self.size + self._gap

    def draw(self, screen: pygame.Surface):
        for i in range(self.rows):
            pygame.draw.rect(screen, tuple(
                self.colors[i]), self.tiles[i])

    # Should only be run once
    def create_grid(self):
        # adjust_mid = (self.rows*self.gap[0] + self.size[0])/2
        self.tiles.append(pygame.Rect((self.pos[0],
                                       self.pos[1],
                                       self.size[0],
                                       self.size[1])))

    def react_to_mouse_overlap(self):
        overlapped_tile = None
        for j in range(self.rows[1]):
            for i in range(self.rows[0]):
                if self.tiles[j][i].collidepoint(pygame.mouse.get_pos()):
                    self.colors[j][i] = self.highlight_color
                    overlapped_tile = (i, j)
                else:
                    self.colors[j][i] = self.default_color

        return overlapped_tile

    def get_overlapped_tile(self):
        """If the overlapped tile is a bomb, then return True"""
        for i in range(self.rows):
            if self.tiles[i].collidepoint(pygame.mouse.get_pos()):
                # Reward coins based on the associated item
                return self.items[i].value * self.items[i].multiplier

        return 0

class UpgradeGrid(Grid):
    def __init__(self, pos, size, rows, color, gap, items):
        super().__init__(pos, size, rows, color, gap, items)

    def get_overlapped_tile(self):
        """Return the item by ID to upgrade."""
        for i in range(self.rows):
            if self.tiles[i].collidepoint(pygame.mouse.get_pos()):
                # Reward coins based on the associated item
                return self.items[i].id

        return -1