from dataclasses import dataclass

@dataclass
class Item:
    id: int
    name: str
    value: int = 0
    upgrade_cost: int = 0
    multiplier: float = 1.0
    multiplier_upgrade_bonus: float = 3.0
    enable_automation: bool = False
    level: int = 0
    
    def upgrade_multiplier(self):
        self.multiplier += self.multiplier_upgrade_bonus
        self.level += 1

class Collector:
    def __init__(self):
        self.gold = 0
        
    