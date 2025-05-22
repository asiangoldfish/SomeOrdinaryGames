import numpy as np
import pygame

import error
import item as inventory_item

import random
random.seed(5)


class Inventory:
    def __init__(self, pos, size, divisions, color, gap):
        if size.size != 2:
            print("Size must be 2")
        elif size[0] < 1:
            print("There must be at least 1 horizontal tile(s)")
        elif size[1] < 1:
            print("There must be at least 1 vertical tile(s)")

        self.pos = pos
        self.size = size
        self.divisions = divisions
        self.colors = np.full(
            (divisions[0], divisions[1], 4), color, dtype=np.uint8)

        self.tiles = list()
        self._gap = gap + size
        self.positions = list()

        self.default_color = pygame.Color(70, 30, 50)

        # Logical representation of items in the inventory
        # Layout:
        # [[Item Item]
        #  [Item  None]]
        self.items = np.full(
            (divisions[0], divisions[1]), None, dtype=inventory_item.Item)

    def add_item(self, item: inventory_item.Item = None, item_type: inventory_item.ItemType = None, position: np.array = None) -> bool:
        """Add an item to the inventory.

        Args:
            item (item.Item): Reference to the item to add. Set to None if the item_type is passed instead. Default: None
            item_type (item.ItemType): The item type to add. A new Item object is created. Default. None
            position (np.array): The 2d position to place the item at. If None is passed, then the next available slot is used. Default: None

        Returns:
            (bool, Error): True if the item was successfully added.
        """
        if position[0] >= self.divisions[0] or position[1] >= self.divisions[1]:
            return False, error.Error("Cannot add an item out of the inventory's divisions.", error.ErrorType.FATAL)

        is_slot_found = False
        item_position = np.array((0, 0))

        # Create new item?
        new_item = None
        if item is not None:
            new_item = item
        else:
            if item_type is None:
                return False, error.Error("Argument 'item_type' cannot be None.", error.ErrorType.FATAL)
            else:
                new_item = inventory_item.Item(item_type)

        # Find the next available slot?
        if position is None:
            for j in range(self.divisions[1]):
                for i in range(self.divisions[0]):
                    if self.items[j][i] is None:
                        # Found an available slot
                        self.items[j][i] = new_item
                        item_position = np.array((j, i))
                        is_slot_found = True
                        break
                if is_slot_found:
                    break
        else:
            if self.items[position[1]][position[0]] is None:
                self.items[position[1]][position[0]] = new_item
                item_position = position
                is_slot_found = True
            else:
                return False, error.Error(f"The slot at {position} is already taken.")

        if is_slot_found:
            self.update_slots(item_position)

        return False, error.Error("The inventory is full.")

    @property
    def gap(self):
        return self._gap

    @gap.setter
    def gap(self, new_gap):
        self._gap = self.size + self._gap

    def draw(self, screen: pygame.Surface):
        for j in range(self.divisions[1]):
            for i in range(self.divisions[0]):
                pygame.draw.rect(screen, tuple(
                    self.colors[j][i]), self.tiles[j][i])

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

    def update_slots(self, pos: np.array = None):
        """Update the inventory slots based on items.

        If `pos` is None, then update all slots.

        Args:
            pos (np.array, optional): Update at given position/index. Defaults to None.
        """
        # if pos is None:

        # else:
        selected_item = self.items[pos[1]][pos[0]]
        print(selected_item.update_item())
        self.colors[pos[1]][pos[0]] = selected_item.update_item()

    def __repr__(self):
        return str(self.items)
