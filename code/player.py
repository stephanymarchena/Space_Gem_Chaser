import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, CONTROL_PLAYER_UP, CONTROL_PLAYER_DOWN, CONTROL_PLAYER_LEFT, \
    CONTROL_PLAYER_RIGHT
from code.entity import  Entity


class Player(Entity):

    def __init__(self,name: str, position: tuple):
        super().__init__(name, position)
        self.health = 3


    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[CONTROL_PLAYER_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[CONTROL_PLAYER_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[CONTROL_PLAYER_LEFT[self.name]] and self.rect.left >0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[CONTROL_PLAYER_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]


