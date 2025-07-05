import ui
import game
import core
from core import Vec2, Vec3

import numpy as np
import pygame

import math


class GameMenu(ui.Canvas):
    def __init__(self, items, collector):
        super().__init__()
        self.items = items
        self.collector = collector

        # self.carrot_btn = ui.Button(
        #     pos=Vec2(170, 500), size=Vec2(400, 100), text="Carrots")

        # Create a button for each item
        for i, item in enumerate(self.items):
            button = ui.Button(
                pos=Vec2(170, 500 + i * 110),
                size=Vec2(400, 100),
                text=item.name
            )

            # Bind click to item using a closure (capture item value)
            button.on_click(
                lambda it: self._collect_from_item(*it), item)

            self.ui_elements.append(button)

        # self.upgrade_grid = game.grid.UpgradeGrid(
        #     pos=np.array((600, 500)),
        #     size=np.array([100.0, 100.0]),
        #     rows=1,
        #     color=np.array((0, 0, 0, 255)),
        #     gap=20.0,
        #     items=items)
        # self.upgrade_grid.create_grid()

        self.my_message = core.Message(
            pos=np.array((200, 100)),
            text="Gold: 0"
        )

        # Dirty trick to go back to main menu by registering a handle which the
        # entry script must register.

        self.main_menu_btn = ui.Button(
            Vec2(10, 10), Vec2(100, 100), "<-", Vec3(50, 50, 50))

        self.ui_elements.append(self.main_menu_btn)

    def _collect_from_item(self, item: game.Item):
        new_value = item.value * item.multiplier
        self.collector.gold += new_value
        self.my_message.text = f"Gold: " + str(math.floor(self.collector.gold))

    def handle_events(self, event):
        super().handle_events(event)

        # match event.type:
        # case pygame.MOUSEBUTTONDOWN:
        # Get coins by clicking tile
        # coins_rewarded = self.my_grid.get_overlapped_tile()
        # self.collector.gold += coins_rewarded

        # # Upgrade item multiplier
        # upgrade_item_id = self.upgrade_grid.get_overlapped_tile()
        # if upgrade_item_id >= 0 and self.collector.gold >= self.items[upgrade_item_id].upgrade_cost:
        # self.items[upgrade_item_id].upgrade_multiplier()
        # self.collector.gold -= self.items[upgrade_item_id].upgrade_cost

        # self.my_message.text = "Gold: " + str(self.collector.gold)

    def draw(self, screen):
        super().draw(screen)

        # self.upgrade_grid.draw(screen)
        self.my_message.draw(screen)
