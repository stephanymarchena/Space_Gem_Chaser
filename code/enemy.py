import random
from code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_y = 2  # Velocidade da queda

    def move(self):
        # Movimento horizontal
        self.rect.centerx -= ENTITY_SPEED[self.name]
        # Movimento vertical (queda)
        self.rect.top += self.speed_y

    def take_damage(self):
        """Reduz a vida do inimigo para 0 quando ele colide com o player."""
        self.health = 0  # O inimigo desaparece imediatamente