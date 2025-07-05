import ui
import core


class PauseMenu(ui.Canvas):
    """The in-game menu"""

    def __init__(self):
        super().__init__()

        self.my_message = core.Message(
            pos=core.Vec2(200, 100),
            text="Pause"
        )

        self.save_game_btn = ui.Button(
            pos=core.Vec2(150, 400),
            size=core.Vec2(600, 100),
            text="Save Game")
        self.main_menu_btn = ui.Button(
            pos=core.Vec2(150, 600),
            size=core.Vec2(600, 100),
            text="Return to Main Menu")
        self.ui_elements.extend((self.save_game_btn, self.main_menu_btn))

    def draw(self, screen):
        super().draw(screen)
        self.my_message.draw(screen)
