from abc import abstractmethod
from enum import verify

import pygame

from code.enemy import Enemy
from code.entity import Entity
from code.gem import Gem
from code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, Gem)):
            if ent.rect.bottom and ent.rect.left and ent.rect.right < 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity], player: Player):
        for ent in entity_list[:]:  # Criamos uma cópia para evitar remoção durante iteração
            EntityMediator.__verify_collision_window(ent)

            if isinstance(ent, Gem) and player.rect.colliderect(ent.rect):
                player.add_score(10)  #  metodo de pontuação
                pygame.mixer.Sound('./asset/music/picked_gem.wav').play()  # Som de pegar gema
                ent.health = 0  # Remove a gema

            elif isinstance(ent, Enemy) and player.rect.colliderect(ent.rect):
                pygame.mixer.Sound('./asset/music/damage.wav').play()  # Som de dano SEMPRE toca
                player.health -= 10  # O astronauta perde vida
                if player.score >= 5:
                    player.add_score(-5)  # Subtrai pontos corretamente
                else:
                    player.score = 0  # Mantém a pontuação mínima em 0
                ent.take_damage()  # metodo para remover o inimigo

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Remove entidades com vida zerada."""
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]