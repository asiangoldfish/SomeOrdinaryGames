import ui
import core
import upgradables

import math

class ShopMenu(ui.Canvas):
    def __init__(self, items, collector):
        super().__init__()
        
        self.items = items
        self.collector = collector
        self.upgrade_btns = []

        self.game_menu_btn = ui.Button(
            pos=core.Vec2(10, 10), size=core.Vec2(100, 100), text="<-", font_size=50)
        
        self.current_gold_txt = core.Message(
            pos=core.Vec2(200, 100),
            text="Gold: 0"
        )

        self.ui_elements.append(self.game_menu_btn)

        self.upgradables = []
        for item in self.items:
            self.upgradables.append(upgradables.UpgradableItem(collector, item))
            if not item.is_enabled:
                self.upgradables.append(upgradables.UnlockItem(collector, item))

        self.upgradables.sort(key=lambda e: e.cost)
        self.sync_buttons()

        # Update UI elements every n seconds to prevent lag
        self._update_timer: float = 1.0
        self._current_update_timer: float = self._update_timer

    def _autoclick_item(self, btn, item):
        if self.collector.gold >= item.automation_cost:
            item.enable_automation = True
            self.ui_elements.remove(btn)
            self.collector.gold -= item.automation_cost
            
    def draw(self, screen):
        super().draw(screen)
        self.current_gold_txt.draw(screen)

    def update(self, delta):
        super().update(delta)
        self.current_gold_txt.text = f"Gold: {math.floor(self.collector.gold)}"
        # TODO update the button's enabled or disabled
        for e in self.ui_elements:
            try:
                e.is_enabled = e.upgradable.can_afford()
            except AttributeError:
                continue
    
    def sync_buttons(self):
        # Create a button for each item
        for i, upgradable in enumerate(self.upgradables):
            button = ui.Button(
                pos=core.Vec2(100, 300 + i * 110),
                size=core.Vec2(600, 100),
                text=upgradable.name
            )
            button.upgradable = upgradable

            # In the future, if we need to specifically do something with
            # certain elements and not all, a new list for those items should
            # probably be created.
            self.ui_elements.append(button)

            # TODO: Fix on_click so the button is either removed if
            # Upgradable.is_repeatable is False, or reorder the list if it is
            # True.
            button.on_click(lambda a: upgradable.activate(), None)