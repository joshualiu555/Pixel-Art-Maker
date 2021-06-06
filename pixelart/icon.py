import pygame as pg
from constants import *

class Icon(pg.sprite.DirtySprite):
    def __init__(self, image_name, tool_name, x, y, gap):
        pg.sprite.DirtySprite.__init__(self)
        self.image_name = image_name
        self.tool_name = tool_name
        self.x, self.y = x * (ICON_SIZE + gap) + 25, y * (ICON_SIZE + gap) + 30
        self.image = pg.transform.scale(self.image_name, (ICON_SIZE, ICON_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.selected = False

    def draw_border(self, screen):
        if self.selected:
            # pygame doesn't allow you draw rectangle border, so you just have to draw 4 lines
            pg.draw.rect(screen, WHITE, (self.rect.topleft[0], self.rect.topleft[1], ICON_SIZE, 5))
            pg.draw.rect(screen, WHITE, (self.rect.bottomleft[0], self.rect.bottomleft[1], ICON_SIZE + 5, 5))
            pg.draw.rect(screen, WHITE, (self.rect.topleft[0], self.rect.topleft[1], 5, ICON_SIZE))
            pg.draw.rect(screen, WHITE, (self.rect.topright[0], self.rect.topright[1], 5, ICON_SIZE))
