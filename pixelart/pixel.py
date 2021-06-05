import pygame as pg
from constants import *

class Pixel(pg.sprite.DirtySprite):
    def __init__(self, color, x, y):
        pg.sprite.DirtySprite.__init__(self)
        self.color = color
        self.x, self.y = x, y
        self.image = pg.Surface((PIXEL_SIZE, PIXEL_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * PIXEL_SIZE + WIDTH / 3, y * PIXEL_SIZE

    def change_color(self, color):
        self.color = color
        self.image.fill(color)
