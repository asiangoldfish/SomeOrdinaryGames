import pygame
import numpy as np
from .base_ui import BaseUI

# TODO: Add support for images and text
class Button(BaseUI):
    def __init__(self, x, y, size_x, size_y, color: tuple):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

        self.shape = pygame.Rect((self.x, self.y, self.size_x, self.size_y))

        self.is_mouse_hovered = False
        self.is_mouse_clicked = False  # Single click registered

        self._on_hover_handle = None
        self._on_hover_args = []
        self._on_press_handle = None
        self._on_press_args = []
        self._on_click_handle = None
        self.on_click_args = []

    def update(self):
        self.is_mouse_hovered = self.shape.collidepoint(pygame.mouse.get_pos())

        if self.is_mouse_hovered:
            if self._on_hover_handle:
                self._on_hover_handle(self._on_hover_args)

            if self._on_press_handle and pygame.mouse.get_pressed()[0]:
                self._on_press_handle(self._on_press_args)

    def handle_events(self, event):

        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self._on_click_handle and self.is_mouse_hovered:
                    self._on_click_handle(self._on_click_args)


    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color,
                         self.shape)

    ##########################################
    # Handlers
    ##########################################

    def on_hover(self, func, *args):
        self._on_hover_handle = func
        self._on_hover_args = args

    def on_press(self, func, *args):
        self._on_press_handle = func
        self._on_press_args = args

    def on_click(self, func, *args):
        self._on_click_handle = func
        self._on_click_args = args