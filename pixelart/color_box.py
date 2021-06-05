import pygame as pg
from constants import *

class ColorBox(pg.sprite.DirtySprite):
    def __init__(self, color, x, y, gap):
        pg.sprite.DirtySprite.__init__(self)
        self.color = color
        self.x, self.y = x, y
        self.image = pg.Surface((COLOR_BOX_SIZE, COLOR_BOX_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * (COLOR_BOX_SIZE + gap) + 40, y * (COLOR_BOX_SIZE + gap) + 475
        self.selected = False

    def draw_circle(self, screen):
        if self.selected:
            if self.color != WHITE:
                pg.draw.circle(screen, WHITE, self.rect.center, 20)
            else:
                pg.draw.circle(screen, BLACK, self.rect.center, 20)
