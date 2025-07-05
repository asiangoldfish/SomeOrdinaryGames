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

        self.play_game_btn = ui.Button(pos=core.Vec2(150, 400), size=core.Vec2(
            500, 100), text="Play")
        self.quit_game_btn = ui.Button(pos=core.Vec2(150, 600), size=core.Vec2(
            500, 100), text="Quit")
        self.ui_elements.extend((self.play_game_btn, self.quit_game_btn))

    def draw(self, screen):
        super().draw(screen)
        self.my_message.draw(screen)
