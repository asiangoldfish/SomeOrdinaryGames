import pygame
import numpy as np

import core.app as app
import sprite
import game
import core.message as message

import atexit

my_app = app.App()
atexit.register(my_app.at_exit)

floor = my_app.SCREEN_HEIGHT - 100

items = [
    game.Item(
        id=0,
        name="Carrots",
        value=1,
        upgrade_cost=10,
        multiplier_upgrade_bonus=3.0
    )
]
collector = game.Collector()

my_grid = game.grid.Grid(
    pos = np.array((170, 500)),
    size=np.array([400.0, 100.0]),
    rows = 1,
    color=np.array((0,0,0,255)),
    gap = 20.0,
    items=items)
my_grid.create_grid()

upgrade_grid = game.grid.UpgradeGrid(
    pos = np.array((600, 500)),
    size=np.array([100.0, 100.0]),
    rows = 1,
    color=np.array((0,0,0,255)),
    gap = 20.0,
    items=items)
upgrade_grid.create_grid()

my_message = message.Message(
    pos=np.array((200,100)),
    text="0"
)

while not my_app.is_closing:
    my_app.screen.fill((127, 127, 127))

    # Handle events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                my_app.is_closing = True
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    my_app.is_closing = True
                elif event.key == pygame.K_SPACE:
                    collector.gold += collector.carrots.value
                    
                    my_message.text = str(collector.gold)

            # Select tile
            case pygame.MOUSEBUTTONDOWN:
                # Get coins by clicking tile
                coins_rewarded = my_grid.get_overlapped_tile()
                collector.gold += coins_rewarded
                
                # Upgrade item multiplier
                upgrade_item_id = upgrade_grid.get_overlapped_tile()
                if upgrade_item_id >= 0 and collector.gold >= items[upgrade_item_id].upgrade_cost:
                    items[upgrade_item_id].upgrade_multiplier()
                    collector.gold -= items[upgrade_item_id].upgrade_cost
                
                my_message.text = str(collector.gold)
                    
                
    my_grid.draw(my_app.screen)
    upgrade_grid.draw(my_app.screen)

    my_message.draw(my_app.screen)

    pygame.display.update()

    my_app.delta = my_app.clock.tick(60) / 1000
    
        