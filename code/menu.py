import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_WHITE, WIN_WIDTH, C_CYAN, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Bg_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/music/SpaceJazz.mp3')
        pygame.mixer_music.play(-1)  # -1 musica permanece tocando

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenhando a imagem na tela.
            self.menu_text(
                font_path="./asset/fonts/Fredoka-Bold.ttf",
                text_size=50,
                text="SPACE",
                text_color=C_WHITE,
                text_center_pos=((WIN_WIDTH / 2), 70)
            )

            self.menu_text(
                font_path="./asset/fonts/Fredoka-Bold.ttf",
                text_size=50,
                text="GEM CHASER",
                text_color=C_WHITE,
                text_center_pos=((WIN_WIDTH / 2), 120)
            )

            for i in range(len(MENU_OPTION)):
                self.menu_text(
                    font_path="./asset/fonts/Fredoka-SemiBold.ttf",
                    text_size=36,
                    text=MENU_OPTION[i],
                    text_color=C_CYAN,
                    text_center_pos=(400, 300 + 50 * i)
                    # Offset para posicionar um item abaixo do outro a cada iteração
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    # Função para formatação de texto
    def menu_text(self, font_path: str, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font(font_path, text_size)  # Carregar fonte personalizada
        text_surf = text_font.render(text, True, text_color).convert_alpha()  # Criar superfície do texto
        text_rect = text_surf.get_rect(center=text_center_pos)  # Centralizar o texto
        self.window.blit(source=text_surf, dest=text_rect)  # Renderizar texto na tela com o blit
