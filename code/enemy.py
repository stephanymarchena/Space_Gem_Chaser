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

        # Se o inimigo sair da tela pela direita, reposiciona-o na tela
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

        # Se o inimigo ultrapassar o fundo da tela, reposiciona-o no topo
        if self.rect.top > WIN_HEIGHT:
            self.rect.top = -50  # Volta para o topo
            self.rect.centerx = random.randint(40, WIN_WIDTH - 40)  # Randomiza a posição X novamente
