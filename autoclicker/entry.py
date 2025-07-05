import pygame
import numpy as np

import core.app as app
import sprite
import game
import core.message as message
import ui
import menus

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

##########
# Canvas
##########

game_menu = menus.GameMenu(items, collector)
main_menu = menus.MainMenu()
active_menu = game_menu

def switch_to_main_menu(arg):
    global active_menu
    active_menu = main_menu
    print("Switching to main menu")

game_menu.register_main_menu_callback(switch_to_main_menu, None)

# my_button = ui.Button(100, 400, 200, 600, (128, 50, 30))
# my_button.on_click(lambda a: print("Clicked"))
# my_button.on_hover(lambda a: print("Hovering"))  # Testing button handlers
# my_button.on_press(lambda a: print("Pressed"))  # Testing button handlers

while not my_app.is_closing:
    my_app.screen.fill((127, 127, 127))

    # Update
    # my_button.update()
    active_menu.update()

    # Handle events
    for event in pygame.event.get():
        # my_button.handle_events(event)

        active_menu.handle_events(event)

        match event.type:
            case pygame.QUIT:
                my_app.is_closing = True
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    my_app.is_closing = True

    # Draw
    active_menu.draw(my_app.screen)

    pygame.display.update()

    my_app.delta = my_app.clock.tick(60) / 1000
