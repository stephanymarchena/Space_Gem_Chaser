from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'bg_':
                list_bg = []  # Inicializa a lista antes do loop
                for i in range(1,6):
                    list_bg.append(Background(f'bg_{i}', (0, 0)))
                    list_bg.append(Background(f'bg_{i}', (WIN_WIDTH, 0)))
                return list_bg  # Retorna a lista completa após o loop
