import game
import core

class Upgradable:
    def __init__(self, collector: game.Collector):
        self.is_repeatable: bool = False  # True if this can be bought again
        self.cost: float = 0
        self.name: str = ""
        self.collector = collector

        self.disabled_color = core.Vec3(70)
        self.enabled_color = core.Vec3(150)

    def activate(self):
        """Action whenever the upgradable is activated.
        """
        pass

    def can_afford(self):
        return self.collector.gold >= self.cost

class UpgradableItem(Upgradable):
    def __init__(self, collector: game.Collector, item: game.Item):
        super().__init__(collector)
        self.item: game.Item = item
        self.is_repeatable = True
        self.cost = item.upgrade_cost
        self.name = f"Autoclick {item.name} ({self.cost})"
    
    def activate(self):
        self.item.upgrade_multiplier()

class UnlockItem(Upgradable):
    def __init__(self, collector: game.Collector, item: game.Item):
        super().__init__(collector)
        self.item: game.Item = item
        self.cost = item.unlock_cost
        self.name = f"Unlock {item.name} ({self.cost})"
    
    def activate(self):
        self.item.is_enabled = True