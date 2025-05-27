import pygame
import numpy as np

import sprite
import inventory
import message
import error
import item

# Initialization
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

my_inventory = inventory.Inventory(
    pos=np.array((170, 500)),
    size=np.array([100.0, 100.0]),
    divisions=np.array((4, 4)),
    color=pygame.Color(0, 0, 0),
    gap=20.0)

crafting_table = inventory.Inventory(
    pos=np.array((170, 200)),
    size=np.array((100, 100)),
    divisions=np.array((2, 1)),
    color=pygame.Color(0, 0, 0),
    gap=20.0)

crafting_output = inventory.Inventory(
    pos=np.array((540, 200)),
    size=np.array((100, 100)),
    divisions=np.array((1, 1)),
    color=pygame.Color(0, 0, 0),
    gap=0
)

my_message = message.Message(
    pos=np.array((200, 100)),
    text="Crafting Table")

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
                if event.key == pygame.K_SPACE:
                    my_inventory.add_item(
                        item_type=item.ItemType.WOOD)

            # Select tile
            case pygame.MOUSEBUTTONDOWN:
                # Move item from inventory to crafting table
                selected_inventory_item, position = my_inventory.get_overlapped_tile()
                if selected_inventory_item:
                    # Return back to inventory if the crafting table is full
                    selected_inventory_item, _ = crafting_table.add_item(selected_inventory_item)
                    my_inventory.add_item(
                        item=selected_inventory_item,
                        position=position
                    )
                elif position is not None:
                    # Put item back to inventory if the crafting table is full
                    my_inventory.add_item(
                        item=selected_inventory_item,
                        position=position
                    )

                crafting_table_item, position = crafting_table.get_overlapped_tile()
                if crafting_table_item:
                    my_inventory.add_item(selected_inventory_item)

    my_inventory.draw(screen)
    crafting_table.draw(screen)
    crafting_output.draw(screen)

    # my_message.draw(screen)

    pygame.display.update()

    delta = clock.tick(60) / 1000

pygame.quit()
