
class Canvas:
    """
    A Canvas is an abstraction of a scene.

    By abstracting game logic and elements into canvases, it makes transitioning
    between scenes easier.
    """

    def __init__(self):
        self.ui_elements = []

    def update(self):
        for e in self.ui_elements:
            e.update()


    def handle_events(self, event):
        for e in self.ui_elements:
            e.handle_events(event)

    def draw(self, screen):
        for e in self.ui_elements:
            e.draw(screen)
