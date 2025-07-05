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

    def draw(self, screen):
        self.my_message.draw(screen)