import numpy as np
import pygame

import error
import item as inventory_item

import random
random.seed(5)


class Inventory:
    """The main class of the game. Contains and handles all items.

    The `Inventory` consists of three sub-inventory:
        - main_inventory
        - crafting_inventory
        - output_inventory
    
    
    """

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
        self.default_color = pygame.Color(0,0,0)
        self.colors = [[self.default_color for m in range(divisions[0])] for n in range(divisions[1])]

        self.tiles = list()
        self._gap = gap + size
        self.positions = list()


        # Logical representation of items in the inventory
        # Layout:
        # [[Item Item]
        #  [Item  None]]
        self.items = [[None for m in range(divisions[0])] for n in range(divisions[1])]
        
        self._create_grid()

    def add_item(self, item: inventory_item.Item = None, item_type: inventory_item.ItemType = None, position: np.array = None) -> tuple[inventory_item.Item, error.Error]:
        """Add an item to the inventory.

        Possible inputs and how they are handled:
            1. Both `item` and item_type are passed: Only add the `item` to the
               inventory.
            2. Only `item` is passed: Add it to the inventory.
            3. Only `item_type` is passed: Create a new reference to an `item`
               by the given `item_type` and add it to the inventory. awdawd asd awd 
            4. No `item` or `item_type` is passed: Nothing is added.
        
        If no position is passed, then the next available slot is used.

        Args:
            item (Item): Reference to the item to add. Set to None if the 
                         item_type is passed instead. Default: None
            item_type (ItemType): The item type to add. A new Item object is 
                                  created. Default. None
            position (np.array): The 2d position to place the item at. If None 
                                 is passed, then the next available slot is
                                 used. Default: None

        Returns:
            (Item, Error): Reference to the inventory if it failed to be added.
        """
        if item is None and item_type is None:
            # Case 4: Nothing is added
            return None, error.Error("Neither item or item_type was passed.")
        elif position is not None and (position[0] >= self.divisions[0] or position[1] >= self.divisions[1]):
            # The position is out of bounds
            return None, error.Error("Cannot add an item out of the inventory's divisions.", error.ErrorType.FATAL)

        is_slot_found = False

        # Create new item?
        new_item = None
        if item is not None:
            # Case 2: Only the item is passed
            new_item = item
        else:
            # Case 3: The item_type was passed
            new_item = inventory_item.Item(item_type)

        # Suppose a new item is ready to be added
        if position is None:
            # Add to the next available slot
            for j in range(self.divisions[1]):
                for i in range(self.divisions[0]):
                    if self.items[j][i] is None:
                        # Found an available slot
                        self.items[j][i] = new_item
                        position = np.array((i, j))
                        is_slot_found = True
                        break
                if is_slot_found:
                    break
        else:
            if self.items[position[1]][position[0]] is None:
                self.items[position[1]][position[0]] = new_item
                is_slot_found = True
            else:
                return new_item, error.Error(f"The slot at {position} is already taken.")

        if is_slot_found:
            self.update_slots(position)
        else:
            return None, None
        
        return new_item, error.Error("The inventory is full.")

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
    def _create_grid(self):
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
        """Highlight overlapped tile"""
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
        """Return the overlapped tile"""
        for j in range(self.divisions[1]):
            for i in range(self.divisions[0]):
                if self.tiles[j][i].collidepoint(pygame.mouse.get_pos()):
                    return self.remove_item([i, j]), [i, j]

        return None, None

    def update_slots(self, pos: np.array = None):
        """Update the inventory slots based on items.

        If `pos` is None, then update all slots.

        Args:
            pos (np.array, optional): Update at given position/index. Defaults to None.
        """
        # if pos is None:

        # else:
        selected_item = None
        if self.items[pos[1]][pos[0]] is None:
            self.colors[pos[1]][pos[0]] = self.default_color
            return
        
        selected_item = self.items[pos[1]][pos[0]]
        self.colors[pos[1]][pos[0]] = selected_item.update_item()

    def remove_item(self, pos: list) -> inventory_item.Item:
        selected_item = None
        if self.items[pos[1]][pos[0]] is not None:
            selected_item = self.items[pos[1]][pos[0]]
            self.items[pos[1]][pos[0]] = None
            self.update_slots(pos)
        return selected_item

    def __repr__(self):
        return str(self.items)
