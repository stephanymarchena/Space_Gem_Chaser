import sys

import pygame.display
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.const import C_WHITE, WIN_HEIGHT
from code.entity import Entity


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg_'))
        self.timeout = 2000  # 20 segundos

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

            # printed text
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            C_WHITE, (10, 5))
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'fps: {clock_game.get_fps(): .0f}', C_WHITE,
                            (10, WIN_HEIGHT - 35))
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14, f'entidades: {len(self.entity_list)}', C_WHITE,
                            (10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)  # Carrega a fonte do caminho
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
