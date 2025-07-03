import pygame


class App:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 1000
        self.is_closing = False
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Cube game")
        pygame.mouse.set_pos((300, 300))
        # Set mouse position to middle of screen
        # pygame.event.set_grab(True)
        


    def at_exit(self):
        print("Quitting the application...")
        pygame.quit()
