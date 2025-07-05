import ui
import core

import numpy as np


class MainMenu(ui.Canvas):
    def __init__(self):
        super().__init__()

        self.my_message = core.Message(
            pos=np.array((200, 100)),
            text="Main Menu"
        )

        self.play_game_btn = ui.Button(150, 400, 500, 100, (50, 50, 50))
        self.quit_game_btn = ui.Button(150, 600, 500, 100, (50, 50, 50))
        self.ui_elements.extend((self.play_game_btn, self.quit_game_btn))

    def draw(self, screen):
        super().draw(screen)
        self.my_message.draw(screen)
