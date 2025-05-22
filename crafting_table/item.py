import pygame
import numpy

from enum import Enum

class ItemType(Enum):
    WOOD=0
    COAL=1
    STONE=2


class Item:
    def __init__(self, item_type: ItemType):
        self.item_type = item_type
        self.color = pygame.Color(250,0,0)

        self.update_item()

    def update_item(self) -> pygame.Color:
        """Update the item's thumbnail based on its type"""
        new_color = pygame.Color(0,0,0)
        match(self.item_type):
            case ItemType.WOOD:
                new_color = pygame.Color(180,120,73)
            case ItemType.COAL:
                new_color = pygame.Color(30,30,30)
            case ItemType.STONE:
                new_color = pygame.Color(150,150,150)

        self.color = new_color
        return new_color