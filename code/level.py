import random
import sys

import pygame.display
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, EVENT_GEMS, SPAWN_TIME_GEMS, WIN_WIDTH
from code.entity import Entity


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg_'))
        self.entity_list.append(EntityFactory.get_entity('astronaut_1'))
        self.timeout = 2000  # 20 segundos

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_GEMS, SPAWN_TIME_GEMS)

    def run(self):
        pygame.mixer_music.load('./asset/music/PhantomFromSpace.mp3')
        pygame.mixer_music.play(-1)  # -1 faz a música tocar em loop
        clock_game = pygame.time.Clock()

        while True:
            clock_game.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()  # movimentando o background

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type ==  EVENT_ENEMY:
                    choice = random.choice(('enemy_1', 'enemy_2', 'enemy_5'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_GEMS:
                    gem_name = f'gem_{random.randint(1, 3)}'  # Escolhe uma gema aleatória
                    gem = EntityFactory.get_entity(gem_name)

                    if gem:
                        # Ajusta a posição da gema para evitar sobreposição com outras entidades
                        gem.rect.centerx = random.randint(40, WIN_WIDTH - 40)
                        gem.rect.top = -50  # Inicia no topo da tela
                        self.entity_list.append(gem)  # Adiciona a gema à lista

            # Exibindo HUD na tela.
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            C_WHITE, (10, 5))
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'fps: {clock_game.get_fps(): .0f}', C_WHITE,
                            (10, WIN_HEIGHT - 35))
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            #EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)  # Carrega a fonte de alguma pasta
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
