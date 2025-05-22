import pygame
import numpy as np

import sprite
import grid
import message

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cube game")

# Set mouse position to middle of screen
# pygame.event.set_grab(True)
pygame.mouse.set_pos((300, 300))

floor = SCREEN_HEIGHT - 100

is_closing = False

clock = pygame.time.Clock()
delta = 0.0

my_grid = grid.Grid(
    pos = np.array((170, 500)),
    size=np.array([100.0, 100.0]),
    divisions=np.array((4, 4)),
    color=np.array((0,0,0,255)),
    gap = 20.0,
    bomb_chance=0.3)
my_grid.create_grid()

my_message = message.Message(
    pos=np.array((200,100)),
    text="The Fake Minesweeper"
)

while not is_closing:
    screen.fill((127, 127, 127))

    # Handle events
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                is_closing = True
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_closing = True

            # Select tile
            case pygame.MOUSEBUTTONDOWN:
                is_bomb_tile, tile_index = my_grid.get_overlapped_tile()
                if tile_index is not None:
                    my_grid.colors[tile_index[0]][tile_index[1]] = my_grid.default_color
                    if is_bomb_tile:
                        my_message.text = "Game over!"
                        my_grid.colors[tile_index[0]][tile_index[1]] = my_grid.highlight_color
                



    my_grid.draw(screen)

    my_message.draw(screen)

    pygame.display.update()

    delta = clock.tick(60) / 1000

pygame.quit()
