import ui
import game
import numpy as np

import pygame

import core


class GameMenu(ui.Canvas):
    def __init__(self, items, collector):
        super().__init__()
        self.items = items
        self.collector = collector

        self.my_grid = game.grid.Grid(
            pos=np.array((170, 500)),
            size=np.array([400.0, 100.0]),
            rows=1,
            color=np.array((0, 0, 0, 255)),
            gap=20.0,
            items=items)
        self.my_grid.create_grid()

        self.upgrade_grid = game.grid.UpgradeGrid(
            pos=np.array((600, 500)),
            size=np.array([100.0, 100.0]),
            rows=1,
            color=np.array((0, 0, 0, 255)),
            gap=20.0,
            items=items)
        self.upgrade_grid.create_grid()

        self.my_message = core.Message(
            pos=np.array((200, 100)),
            text="Gold: 0"
        )

        # Dirty trick to go back to main menu by registering a handle which the
        # entry script must register.

        self.main_menu_btn = ui.Button(10, 10, 100, 100, (50, 50, 50))

        self.ui_elements.append(self.main_menu_btn)

    def handle_events(self, event):
        super().handle_events(event)

        match event.type:
            case pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.collector.gold += self.collector.carrots.value

                    self.my_message.text = "Gold: " + str(self.collector.gold)

            # Select tile
            case pygame.MOUSEBUTTONDOWN:
                # Get coins by clicking tile
                coins_rewarded = self.my_grid.get_overlapped_tile()
                self.collector.gold += coins_rewarded

                # Upgrade item multiplier
                upgrade_item_id = self.upgrade_grid.get_overlapped_tile()
                if upgrade_item_id >= 0 and self.collector.gold >= self.items[upgrade_item_id].upgrade_cost:
                    self.items[upgrade_item_id].upgrade_multiplier()
                    self.collector.gold -= self.items[upgrade_item_id].upgrade_cost

                self.my_message.text = "Gold: " + str(self.collector.gold)

    def draw(self, screen):
        super().draw(screen)

        self.my_grid.draw(screen)
        self.upgrade_grid.draw(screen)
        self.my_message.draw(screen)
