from code.const import WIN_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.gem import Gem

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity, entity_list: list[Entity]):
        """Verifica se uma entidade saiu da tela e a remove se necessário."""
        if isinstance(ent, Gem):  # Apenas as gemas são removidas
            if ent.rect.top > WIN_HEIGHT:  # Saiu pela parte inferior da tela
                entity_list.remove(ent)  # Remove a gema para que outra possa surgir
            elif ent.rect.right < 0:  # Saiu pela esquerda
                entity_list.remove(ent)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        """Verifica todas as entidades e remove as que saíram da tela."""
        for ent in entity_list[:]:  # Criamos uma cópia da lista para evitar problemas ao remover itens
            EntityMediator.__verify_collision_window(ent, entity_list)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        """Remove entidades com vida <= 0 (inimigos mortos)."""
        for ent in entity_list[:]:  # Evita erro de modificação da lista
            if ent.health <= 0:
                entity_list.remove(ent)
