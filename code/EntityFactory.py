import random

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.gem import Gem
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'bg_':
                list_bg = []  # Inicializa a lista antes do loop
                for i in range(1,6):
                    list_bg.append(Background(f'bg_{i}', (0, 0)))
                    list_bg.append(Background(f'bg_{i}', (WIN_WIDTH, 0)))
                return list_bg  # Retorna a lista completa após o loop

            case 'astronaut_1':
                return Player('astronaut_1', (10, WIN_HEIGHT / 2))

            case 'enemy_1':
                return Enemy('enemy_1', (random.randint(40, WIN_WIDTH - 40), -50))  # Inimigo começa de cima

            case 'enemy_2':
                return Enemy('enemy_2', (random.randint(40, WIN_WIDTH - 40), -50))  # Inimigo começa de cima

            case 'enemy_5':
                return Enemy('enemy_5', (random.randint(20, WIN_WIDTH - 40), -50))  # Inimigo começa de cima

            case 'gem_1':
                return Gem('gem_1', (random.randint(20, WIN_WIDTH - 40), -50))

            case 'gem_2':
                return Gem('gem_2', (random.randint(20, WIN_WIDTH - 40), -50))

            case 'gem_3':
                return Gem('gem_3', (random.randint(20, WIN_WIDTH - 40), -50))

            case 'gem_4':
                return Gem('gem_4', (random.randint(20, WIN_WIDTH - 40), -50))