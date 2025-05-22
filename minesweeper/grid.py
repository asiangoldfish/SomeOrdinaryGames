import numpy as np
import pygame

import random
random.seed(5)


class Grid:
    def __init__(self, pos, size, divisions, color, gap, bomb_chance=0.2):
        if size.size != 2:
            print("Size must be 2")
        elif size[0] < 1:
            print("There must be at least 1 horizontal tile(s)")
        elif size[1] < 1:
            print("There must be at least 1 vertical tile(s)")

        self.pos = pos
        self.size = size
        self.divisions = divisions
        self.colors = np.full((divisions[0], divisions[1],4), color, dtype=np.uint8)

        self.tiles = list()
        self._gap = gap + size
        self.positions = list()

        self.highlight_color = pygame.Color("yellow")
        self.default_color = pygame.Color(70,30,50)


        # TODO find some way to reduce the duplication
        self.bomb_chance = bomb_chance
        self.bombs = np.random.rand(self.divisions[1], self.divisions[0])
        self.bombs = self.bombs < self.bomb_chance

        generations = 0

        while not self.bombs.any(where=True):
            generations += 1
            self.bombs = np.random.rand(self.divisions[1], self.divisions[0])
            self.bombs = self.bombs < self.bomb_chance
    

        print(self.bombs, generations)

    @property
    def gap(self):
        return self._gap

    @gap.setter
    def gap(self, new_gap):
        self._gap = self.size + self._gap

    def draw(self, screen: pygame.Surface):
        for j in range(self.divisions[1]):
            for i in range(self.divisions[0]):
                pygame.draw.rect(screen, tuple(self.colors[j][i]), self.tiles[j][i])

    # Should only be run once
    def create_grid(self):
        adjust_mid = (
            (self.divisions[0]*self.gap[0] + self.size[0])/2,
            (self.divisions[1]*self.gap[1] - self.size[1])/2,
        )

        # new_grid = pygame.Rect((pos[0], pos[1], size[0], size[1]))
        for j in range(self.divisions[1]):
            self.positions.append(list())
            self.tiles.append(list())

            for i in range(self.divisions[0]):
                self.positions[j].append(np.array([
                    i * self.gap[0] + self.pos[0], 
                    j * self.gap[1] + self.pos[1]]))
                self.tiles[j].append(pygame.Rect((self.positions[j][i][0],
                                                  self.positions[j][i][1],
                                                  self.size[0],
                                                  self.size[1])))

    def react_to_mouse_overlap(self):
        overlapped_tile = None
        for j in range(self.divisions[1]):
            for i in range(self.divisions[0]):
                if self.tiles[j][i].collidepoint(pygame.mouse.get_pos()):
                    self.colors[j][i] = self.highlight_color
                    overlapped_tile = (i, j)
                else:
                    self.colors[j][i] = self.default_color

        return overlapped_tile
    
    def get_overlapped_tile(self):
        """If the overlapped tile is a bomb, then return True"""
        tile_index = None
        for j in range(self.divisions[1]):
            for i in range(self.divisions[0]):
                if self.tiles[j][i].collidepoint(pygame.mouse.get_pos()):
                    tile_index = (j, i)
                    if self.bombs[j][i]:
                        return True, tile_index
        
        return False, tile_index