import ui
import core

import math

class ShopMenu(ui.Canvas):
    def __init__(self, items, collector):
        super().__init__()
        
        self.items = items
        self.collector = collector

        self.game_menu_btn = ui.Button(
            pos=core.Vec2(10, 10), size=core.Vec2(100, 100), text="<-", font_size=50)
        
        self.current_gold_txt = core.Message(
            pos=core.Vec2(200, 100),
            text="Gold: 0"
        )


        # Create a button for each item
        for i, item in enumerate(self.items):
            button = ui.Button(
                pos=core.Vec2(100, 300 + i * 110),
                size=core.Vec2(600, 100),
                text=f"Autoclick {item.name} ({item.automation_cost})"
            )
            # Bind click to item using a closure (capture item value)
            self.ui_elements.append(button)
            button.on_click(lambda button, it: self._autoclick_item(button, it), button, item)

        self.ui_elements.append(self.game_menu_btn)

    def _autoclick_item(self, btn, item):
        if self.collector.gold >= item.automation_cost:
            item.enable_automation = True
            self.ui_elements.remove(btn)
            self.collector.gold -= item.automation_cost
            
    def draw(self, screen):
        super().draw(screen)
        self.current_gold_txt.text = f"Gold: {math.floor(self.collector.gold)}"
        self.current_gold_txt.draw(screen)