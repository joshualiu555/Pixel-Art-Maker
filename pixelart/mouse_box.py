import pygame as pg
from constants import *

class mouseBox(pg.sprite.DirtySprite):
    def __init__(self, pos, gap):
        pg.sprite.DirtySprite.__init__(self)
        self.image = pg.Surface((MOUSE_BOX_SIZE, MOUSE_BOX_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos * (MOUSE_BOX_SIZE + gap) + 50, 415
        self.selected = False

    def update(self):
        if self.selected:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(0)

