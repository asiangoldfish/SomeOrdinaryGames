import pygame
import numpy as np

import core.app as app
import game
import core.message as message
import menus

import atexit

my_app = app.App()
atexit.register(my_app.at_exit)

floor = my_app.SCREEN_HEIGHT - 100

items = [
    game.Item(
        name="Carrots",
        value=1,
        upgrade_cost=30,
        multiplier_upgrade_bonus=3.0
    ),
    game.Item(
        name="Potatoes",
        value=3,
        upgrade_cost=100,
        multiplier_upgrade_bonus=3.0
    )
]
for i, item in enumerate(items):
    item.id = i
collector = game.Collector()

##########
# Menus
##########

game_menu = menus.GameMenu(items, collector)
main_menu = menus.MainMenu()
pause_menu = menus.PauseMenu()
active_menu = game_menu


def switch_to_main_menu(arg):
    global active_menu
    active_menu = main_menu
    print("Switching to main menu")


def switch_to_play_game(arg):
    global active_menu
    active_menu = game_menu
    print("Switching to play game")


def quit_game_handler(arg):
    global my_app
    my_app.is_closing = True

def save_game_handler(arg):
    print("Game saved!")


game_menu.main_menu_btn.on_click(switch_to_main_menu, None)
main_menu.play_game_btn.on_click(switch_to_play_game, None)
main_menu.quit_game_btn.on_click(quit_game_handler, None)
pause_menu.main_menu_btn.on_click(switch_to_main_menu, None)
pause_menu.save_game_btn.on_click(save_game_handler, None)

while not my_app.is_closing:
    my_app.screen.fill((127, 127, 127))

    # Update
    active_menu.update()

    # Handle events
    for event in pygame.event.get():
        active_menu.handle_events(event)

        match event.type:
            case pygame.QUIT:
                my_app.is_closing = True
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # While in-game, toggle between the game and the pause menu.
                    if active_menu is game_menu:
                        active_menu = pause_mmenu
                    elif active_menu is pause_mmenu:
                        active_menu = game_menu

    # Draw
    active_menu.draw(my_app.screen)

    pygame.display.update()

    my_app.delta = my_app.clock.tick(60) / 1000
