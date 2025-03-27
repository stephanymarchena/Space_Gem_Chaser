import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run() #Variável que faz conexão com o menu do game pelo RETURN na classe menu

            if menu_return == MENU_OPTION[: -1]: # Sendo sempre a última opção o EXIT
                pygame.quit()  # Fecha a janela
                quit()  # Encerra o pygame

            elif menu_return in MENU_OPTION[:-1]: # Todas a opções antes do último item (caso tenha + opções no menu)
                level_game = Level(self.window, 'Level1', menu_return)
                level_return = level_game.run()

            else:
                pass