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
        self.item_btns = []
        self.upgrade_btns = []
        self.disable_upgrade_colour = Vec3(30, 30, 10)
        self.enable_upgrade_color = Vec3(127, 100, 50)
        self.disable_text = Vec3(70)
        self.enable_text = Vec3(150)

        # Create a button for each item
        for i, item in enumerate(self.items):
            button = ui.Button(
                pos=Vec2(70, 500 + i * 110),
                size=Vec2(400, 100),
                text=item.name,
                font_size=40
            )
            # Bind click to item using a closure (capture item value)
            button.on_click(lambda it: self._collect_from_item(it), item)
            self.ui_elements.append(button)
            self.item_btns.append(button)

        # Upgrade button for each item
        for i, item in enumerate(self.items):
            button = ui.Button(
                pos=Vec2(500, 500 + i * 110),
                size=Vec2(270, 100),
                text=f"Lv{str(item.level)} ({str(math.floor(item.upgrade_cost))})",
                bg_color=self.disable_upgrade_colour,
                fg_color=self.disable_text
            )
            button.on_click(
                lambda item, button: self._upgrade_item(item, button), item, button)
            self.ui_elements.append(button)
            self.upgrade_btns.append(button)

        self.my_message = core.Message(
            pos=np.array((200, 100)),
            text="Gold: 0"
        )

        self.main_menu_btn = ui.Button(
            pos=Vec2(10, 10), size=Vec2(100, 100), text="<-", font_size=50)

        self.upgrade_menu_btn = ui.Button(
            pos=Vec2(690, 10), size=Vec2(100, 100), text="+")

        self.ui_elements.extend((self.main_menu_btn, self.upgrade_menu_btn))

    def _update_upgrade_btn_color(self):
        for i, btn in enumerate(self.upgrade_btns):
            if self.collector.gold < self.items[i].upgrade_cost:
                btn.bg_color = self.disable_upgrade_colour
                btn.fg_color = self.disable_text
            else:
                btn.bg_color = self.enable_upgrade_color
                btn.fg_coclor = self.enable_text

    def _collect_from_item(self, item: game.Item):
        new_value = item.value * item.multiplier
        self.collector.gold += new_value
        self._update_upgrade_btn_color()

    def _upgrade_item(self, item: game.Item, button: ui.Button):
        if self.collector.gold >= item.upgrade_cost:
            item.upgrade_multiplier()
            button.text = f"Lv{str(item.level)} ({str(math.floor(item.upgrade_cost))})"
            self.collector.gold -= item.upgrade_cost
            self._update_upgrade_btn_color()

    def handle_events(self, event):
        super().handle_events(event)

    def draw(self, screen):
        super().draw(screen)
        self.my_message.draw(screen)

    def update(self):
        super().update()
        self.my_message.text = f"Gold: {math.floor(self.collector.gold)}"

        for i, item in enumerate(self.items):
            if item.enable_automation:
                self.item_btns[i].text = f"{item.name} ({"{:.2f}".format(item.current_timer)})"

