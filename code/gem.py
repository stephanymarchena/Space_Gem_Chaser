from code.const import ENTITY_SPEED
from code.entity import Entity

class Gem(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_y = ENTITY_SPEED.get(name, 1)  # Usa 1 como valor padrão se o nome não existir

    def move(self):
        self.rect.top += self.speed_y

    def kill(self, entity_list: list):
        """Remove a gema da lista de entidades."""
        if self in entity_list:
            entity_list.remove(self)