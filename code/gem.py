from code.const import WIN_HEIGHT
from code.entity import Entity

class Gem(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_y = 2  # Velocidade de queda da gema

    def move(self):
        self.rect.top += self.speed_y

    def kill(self, entity_list: list):
        """Remove a gema da lista de entidades."""
        if self in entity_list:
            entity_list.remove(self)