from .base_ui import BaseUI
from core import Vec2, Vec3

import pygame

import numpy as np

# TODO: Add support for images and text


class Button(BaseUI):
    def __init__(self, pos: Vec2, size: Vec2, text: str = "", fg_color: Vec3 = Vec3(255, 255, 255), bg_color: Vec3 = Vec3(50,50,50)):
        # https://stackoverflow.com/a/63763175
        self.pos = pos
        self.size = size
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.text = text
        self.text_offset = Vec2(1, 5)
        self.font = pygame.font.Font(
            pygame.font.get_default_font(), (self.size/2).y)
        self.font_surface = self.font.render(f"{text}", True, fg_color.to_tuple())
        self.surface = pygame.Surface((*self.size,)).convert()
        self.surface.fill(self.bg_color.to_tuple())

        self.is_mouse_hovered = False
        self.is_mouse_clicked = False  # Single click registered

        self._on_hover_handle = None
        self._on_hover_args = []
        self._on_press_handle = None
        self._on_press_args = []
        self._on_click_handle = None
        self.on_click_args = []

    def update(self):
        self.is_mouse_hovered = self.surface.get_rect(
            topleft=tuple(self.pos)).collidepoint(pygame.mouse.get_pos())

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
        screen.blit(self.surface, ((*self.pos,)))
        screen.blit(self.font_surface, (self.pos + self.text_offset).to_tuple())

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
