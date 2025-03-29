from abc import ABC, abstractmethod

import pygame.image

from code.const import ENTITY_HEALTH


#from code.const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        # Caminho para carregar as imagens
        self.surf = pygame.image.load('./asset/images/' + name + '.png') .convert_alpha() #--> deixou o bg muito mais rápido
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        #self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, entity_list: list): #verificar o parâmetro entity_list
        pass
