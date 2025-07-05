from dataclasses import dataclass


@dataclass
class Item:
    name: str
    id: int = 0
    value: int = 0
    upgrade_cost: int = 0
    multiplier: float = 1.0
    multiplier_upgrade_bonus: float = 3.0
    enable_automation: bool = False
    automation_cost: int = 10
    level: int = 0

    # Timer settings for autoclick
    current_timer: float = 0.0
    autoclick_cooldown: float = 3.0

    def upgrade_multiplier(self):
        self.multiplier += self.multiplier_upgrade_bonus
        self.level += 1


class Collector:
    def __init__(self, items):
        self.gold = 0
        self.items = items

    def update(self, delta):
        self.autoclick_items(delta)

    def autoclick_items(self, delta):
        """Autoclick items that have unlocked the corresponding upgrade.
        """

        for item in self.items:
            if not item.enable_automation:
                continue
            
            item.current_timer -= delta

            if item.current_timer < 0.0:
                self.gold += item.value * item.multiplier
                item.current_timer = item.autoclick_cooldown

        
