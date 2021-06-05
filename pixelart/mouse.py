import pygame as pg
from constants import *
import math

class Mouse(pg.sprite.DirtySprite):
    def __init__(self, size, color):
        pg.sprite.DirtySprite.__init__(self)
        self.size = size
        self.image = pg.Surface((PIXEL_SIZE * size, PIXEL_SIZE * size))
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.on_board = False

    def update(self):
        mx, my = pg.mouse.get_pos()
        # boundary is the one third mark of the board
        self.on_board = self.rect.left >= int(WIDTH / 3 - 10)
        if self.on_board:
            # rounds the mouse coordinates to the nearest pixel
            self.rect.x, self.rect.y = math.ceil(mx / PIXEL_SIZE) * PIXEL_SIZE, math.ceil(my / PIXEL_SIZE) * PIXEL_SIZE
            self.image.set_colorkey(None)
            pg.mouse.set_cursor(pg.cursors.diamond)
        else:
            self.rect.x, self.rect.y = mx, my
            # make the mouse rect invisible
            self.image.set_colorkey(self.color)
            pg.mouse.set_cursor(pg.cursors.arrow)

    def change_size(self, size):
        self.size = size
        self.image = pg.Surface((PIXEL_SIZE * size, PIXEL_SIZE * size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def change_color(self, color):
        self.color = color
        self.image.fill(color)


