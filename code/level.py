import random
import sys
import time
import pygame.display
from pygame.font import Font

from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.const import (
    C_WHITE, C_RED, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, EVENT_GEM,
    SPAWN_TIME_GEM, WIN_WIDTH, PADDING, C_GREEN, SPACING
)
from code.entity import Entity
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg_'))

        self.player = EntityFactory.get_entity('astronaut_1')
        self.entity_list.append(self.player)

        # Tempo máximo do jogo (60 segundos)
        self.max_time = 60
        self.start_time = time.time()
        self.running = True  # Controle do estado do jogo

        # Variáveis para exibir mensagens de pontuação
        self.damage_text = None
        self.damage_text_timer = 0
        self.score_text = None
        self.score_text_timer = 0

        self.score = 0  # A pontuação do jogador

        # Definição dos eventos de spawn de inimigos e gemas
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_GEM, SPAWN_TIME_GEM)

    def run(self):
        """Executa o loop principal do jogo."""
        pygame.mixer_music.load('./asset/music/PhantomFromSpace.mp3')
        pygame.mixer_music.play(-1)  # -1 faz a música tocar em loop
        clock_game = pygame.time.Clock()

        while self.running:
            clock_game.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela

            elapsed_time = time.time() - self.start_time  # Tempo decorrido

            if elapsed_time >= self.max_time:  # Tempo acabou?
                self.running = False
                break  # Sai do loop do jogo

            # Atualiza e desenha entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # Processamento de eventos
            self.handle_events()

            # Atualiza o HUD
            self.render_hud(clock_game, elapsed_time)

            # Verifica colisões e ajusta a pontuação
            self.handle_collisions()

            # Exibir mensagens de pontuação perto do jogador
            self.display_score_messages()

            # Atualiza a tela
            pygame.display.flip()

            # Remove entidades "mortas"
            EntityMediator.verify_health(entity_list=self.entity_list)

        # Calcula a pontuação final e retorna ao menu
        self.score = self.calculate_score(elapsed_time)
        return 'game_over'

    def handle_events(self):
        """Gerencia eventos do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == EVENT_ENEMY:
                choice = random.choice(('enemy_1', 'enemy_2', 'enemy_5'))
                self.entity_list.append(EntityFactory.get_entity(choice))

            if event.type == EVENT_GEM:
                choice = random.choice(('gem_1', 'gem_2', 'gem_3', 'gem_4'))
                self.entity_list.append(EntityFactory.get_entity(choice))

    def render_hud(self, clock_game, elapsed_time):
        """Renderiza o HUD na tela, alinhando corretamente os elementos."""
        remaining_time = max(self.max_time - elapsed_time, 0)  # Tempo restante

        # Superior esquerdo: Tempo restante
        self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 16,
                        f'Tempo: {remaining_time:.1f}s',
                        C_WHITE, ((PADDING - 70) + (SPACING - 10), PADDING))

        # Superior direito: Score do jogador
        self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 16,
                        f'Score: {self.score}',
                        C_WHITE, ((PADDING - 80) + (SPACING * 2), PADDING))

        # Inferior esquerdo: FPS e quantidade de entidades na tela
        self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14,
                        f'Entidades: {len(self.entity_list)}',
                        C_WHITE, (PADDING + 30, WIN_HEIGHT + 30 - PADDING - 50))

        self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 14,
                        f'FPS: {clock_game.get_fps():.0f}',
                        C_WHITE, (PADDING + 20, (WIN_HEIGHT + 30) - PADDING - 25))

    def handle_collisions(self):
        """Verifica colisões e ajusta a pontuação."""
        player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
        if player:
            old_score = self.score
            EntityMediator.verify_collision(entity_list=self.entity_list, player=player)
            self.score = player.score  # Atualiza a pontuação com a do jogador

            # Exibe "-5" se perdeu pontos
            if self.score < old_score:
                self.damage_text = "-5"
                self.damage_text_timer = 60

            # Exibe "+10" se ganhou pontos
            elif self.score > old_score:
                self.score_text = "+10"
                self.score_text_timer = 60

    def display_score_messages(self):
        """Exibe mensagens temporárias de pontuação (+10 ou -5)."""
        if self.damage_text and self.damage_text_timer > 0:
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 20, self.damage_text, C_RED,
                            (self.player.rect.centerx, self.player.rect.top - 20))
            self.damage_text_timer -= 1
        else:
            self.damage_text = None

        if self.score_text and self.score_text_timer > 0:
            self.level_text("./asset/fonts/Fredoka-SemiBold.ttf", 20, self.score_text, C_GREEN,
                            (self.player.rect.centerx, self.player.rect.top - 40))
            self.score_text_timer -= 1
        else:
            self.score_text = None

    def level_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Exibe um texto na tela."""
        text_font: pygame.font.Font = pygame.font.Font(font_path, text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def calculate_score(self, elapsed_time):
        """Calcula a pontuação final do jogador com base no tempo sobrevivido."""
        return int(elapsed_time * 10)  # Exemplo: 10 pontos por segundo

    def get_score(self):
        """Retorna a pontuação final do jogador."""
        return self.score
