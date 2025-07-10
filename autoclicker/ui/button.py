from .base_ui import BaseUI
from core import Vec2, Vec3

import pygame

import numpy as np

# TODO: Add support for images and text


class Button(BaseUI):
    def __init__(self, pos: Vec2, size: Vec2, text: str = "", fg_color: Vec3 = Vec3(255, 255, 255), bg_color: Vec3 = Vec3(50, 50, 50), font_size=50, id: int = -1):
        # https://stackoverflow.com/a/63763175
        self.id = id
        self.pos = pos
        self.size = size
        self._fg_color = fg_color
        self._bg_color = bg_color
        self._text = text
        self.text_offset = Vec2(1, 5)
        self.font = pygame.font.Font(
            pygame.font.get_default_font(), font_size)
        self.font_surface = self.font.render(
            f"{text}", True, fg_color.to_tuple())
        self.surface = pygame.Surface((*self.size,)).convert()
        self.surface.fill(self.bg_color.to_tuple())

        self._is_enabled = True
        self.disable_upgrade_colour = Vec3(30, 30, 10)
        self.enable_upgrade_color = Vec3(127, 100, 50)
        self.disable_text = Vec3(70)
        self.enable_text = Vec3(150)

        self.is_mouse_hovered = False
        self.is_mouse_clicked = False  # Single click registered

        self._on_hover_handle = None
        self._on_hover_args = []
        self._on_press_handle = None
        self._on_press_args = []
        self._on_click_handle = None
        self.on_click_args = []

    ##########
    # Accessors and mutators
    ##########
    @property
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, new_bg_color):
        self._bg_color = new_bg_color
        self.surface.fill(new_bg_color.to_tuple())

    @property
    def fg_color(self):
        return self._fg_color

    @fg_color.setter
    def fg_color(self, new_color):
        self._fg_color = new_color
        self.font_surface = self.font.render(
            f"{self._text}", True, self.fg_color.to_tuple())

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text
        self.font_surface = self.font.render(
            f"{self._text}", True, self._fg_color.to_tuple())

    @property
    def is_enabled(self):
        return self._is_enabled

    @text.setter
    def is_enabled(self, enable):
        if self._is_enabled is enable:
            pass

        self._is_enabled = enable
        if enable:
            self.font_surface = self.font.render(
                f"{self._text}", True, self.enable_text.to_tuple())
            self.surface.fill(self.enable_upgrade_color.to_tuple())
        else:
            self.font_surface = self.font.render(
                f"{self._text}", True, self.disable_text.to_tuple())
            self.surface.fill(self.disable_upgrade_colour.to_tuple())

    def update(self, delta):
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
                    self._on_click_handle(*self._on_click_args)

    def draw(self, screen: pygame.Surface):
        font_surface_divided = Vec2.from_tuple(self.font_surface.get_size())/2
        screen.blit(self.surface, ((*self.pos,)))

        # Draw the text centralised in the button
        screen.blit(self.font_surface, (self.pos + self.size /
                    2 - font_surface_divided).to_tuple())

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
