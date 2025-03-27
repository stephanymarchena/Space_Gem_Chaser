# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from pygame.locals import QUIT, KEYDOWN, K_DOWN, K_UP, K_RETURN, MOUSEMOTION, MOUSEBUTTONDOWN

from code.const import C_WHITE, WIN_WIDTH, C_CYAN, MENU_OPTION, C_CYAN_2, WIN_HEIGHT


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/images/Bg_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0  # Índice do item selecionado

    def run(self):
        pygame.mixer_music.load('./asset/music/SpaceJazz.mp3')
        pygame.mixer_music.play(-1)  # -1 faz a música tocar em loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem de fundo.

            # Título do jogo
            self.menu_text("./asset/fonts/Fredoka-Bold.ttf", 50, "SPACE", C_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text("./asset/fonts/Fredoka-Bold.ttf", 50, "GEM CHASER", C_WHITE, ((WIN_WIDTH / 2), 120))

            # Desenha o texto do menu
            self.menu_text(
                font_path="./asset/fonts/Fredoka-SemiBold.ttf",
                text_size=14,
                text="Use o mouse ou as setas para navegar // Pressione Enter ou clique para selecionar.",
                text_color=C_CYAN_2,
                text_center_pos=(WIN_WIDTH / 2, 300 + 50 * len(MENU_OPTION) + 30)
            )

            # Carregar imagens para obter largura real
            arrow_img = pygame.image.load('./asset/images/arrows_w.png')
            enter_img = pygame.image.load('./asset/images/enter_w.png')

            # Calcular a largura total do conjunto (seta + enter + espaçamento)
            total_width = arrow_img.get_width() + enter_img.get_width()  # Espaçamento de 10px entre elas
            start_x = (WIN_WIDTH - total_width) / 2  # Centraliza o conjunto de imagens


            # Definir a posição Y abaixo do menu
            pos_y = 300 + 50 * len(MENU_OPTION) + 50  # Ajuste vertical conforme o menu cresce

            # Desenhar as imagens na tela com alinhamento centralizado
            self.draw_arrow_image('./asset/images/arrows_w.png', start_x, pos_y)
            self.draw_arrow_image('./asset/images/enter_w.png', start_x + arrow_img.get_width(), pos_y + 5)

            mouse_x, mouse_y = pygame.mouse.get_pos()  # Pega posição do mouse

            # Exibir opções do menu
            for i, option in enumerate(MENU_OPTION):
                text_color = C_CYAN
                text_rect = self.get_text_rect("./asset/fonts/Fredoka-SemiBold.ttf", 36, option, (400, 300 + 50 * i))

                # Se o mouse estiver sobre a opção, destacamos ela
                if text_rect.collidepoint(mouse_x, mouse_y) or i == self.menu_option:
                    text_color = C_WHITE

                self.menu_text("./asset/fonts/Fredoka-SemiBold.ttf", 36, option, text_color, text_rect.center)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:  # Se alguma tecla for pressionada
                    if event.key == K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)  # Cicla para baixo
                    elif event.key == K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)  # Cicla para cima
                    elif event.key == K_RETURN:  # Tecla ENTER
                        return MENU_OPTION[self.menu_option]

                elif event.type == MOUSEMOTION:
                    for i, option in enumerate(MENU_OPTION):
                        text_rect = self.get_text_rect("./asset/fonts/Fredoka-SemiBold.ttf", 36, option, (400, 300 + 50 * i))
                        if text_rect.collidepoint(event.pos):  # Verifica se o mouse está sobre uma opção
                            self.menu_option = i

                elif event.type == MOUSEBUTTONDOWN:
                    for i, option in enumerate(MENU_OPTION):
                        text_rect = self.get_text_rect("./asset/fonts/Fredoka-SemiBold.ttf", 36, option, (400, 300 + 50 * i))
                        if text_rect.collidepoint(event.pos):  # Se o jogador clicar em uma opção
                            return MENU_OPTION[i]


    # Função para desenhar texto na tela
    def menu_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font(font_path, text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    # Função para obter o retângulo de um texto (ajuda na detecção do mouse)
    def get_text_rect(self, font_path: str, text_size: int, text: str, text_center_pos: tuple):
        text_font = pygame.font.Font(font_path, text_size)
        text_surf = text_font.render(text, True, (0, 0, 0))
        return text_surf.get_rect(center=text_center_pos)

    def draw_arrow_image(self, image_path, x, y):
        arrow_image = pygame.image.load(image_path)
        self.window.blit(arrow_image, (x, y))
