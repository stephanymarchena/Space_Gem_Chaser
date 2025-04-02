import pygame
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()  # Retorna a opção do menu

            if menu_return == MENU_OPTION[-1]:  # Última opção (EXIT)
                pygame.quit()  # Fecha a janela
                quit()  # Encerra o pygame

            elif menu_return in MENU_OPTION[:-1]:  # Opções para o jogo
                level_game = Level(self.window, 'Level1', menu_return)
                level_return = level_game.run()

                if level_return == 'game_over':  # Quando o jogo acabar
                    player_score = level_game.get_score()  # Pega a pontuação do metodo get_score()
                    score = Score(self.window)  # Cria uma instância de Score
                    score.save(player_score)  # Passa a pontuação como argumento para salvar
                    score.show_score()  # Exibe a tela de pontuação

            elif menu_return == MENU_OPTION[2]:  # Ir para a tela de pontuação diretamente
                score = Score(self.window)
                score.show_score()  # Exibe a tela de pontuação
