from abc import abstractmethod
from enum import verify

from code.enemy import Enemy
from code.entity import Entity
from code.gem import Gem


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, Gem)):
            if ent.rect.bottom and ent.rect.left and ent.rect.right < 0:
                ent.health = 0



    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            verify_entity =  entity_list[i]
            # se houver colisão na borda da tela a entidade vai desaparecer
            EntityMediator.__verify_collision_window(verify_entity)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)