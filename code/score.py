import pygame
from pygame import Surface
from datetime import datetime
from code.DBProxy import DBProxy
from code.const import WIN_WIDTH, WIN_HEIGHT

class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/images/bg_save.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def save(self, player_score: int):

        pygame.mixer_music.load('./asset/music/SpaceExplorers.mp3')
        pygame.mixer_music.play(-1)

        """Método para salvar a pontuação no banco de dados."""
        db_proxy = DBProxy('game_scores.db')  # Conecta ao banco de dados
        name = ''  # Inicializa o nome do jogador

        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(48, 'FIM DO JOGO!!', (255, 255, 0), (WIN_WIDTH / 2, WIN_HEIGHT / 4))
            self.score_text(20, 'Enter your name (4 characters, A-Z/0-9):', (255, 255, 255),
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        # Salva a pontuação quando o jogador pressionar Enter
                        score_data = {
                            'name': name,
                            'score': player_score,
                            'date': self.get_formatted_date()
                        }
                        db_proxy.save(score_data)  # Salva no banco de dados
                        return  # Sai da função após salvar
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]  # Apaga o último caractere
                    elif len(name) < 4 and event.unicode.isalnum():
                        name += event.unicode.upper()  # Apenas letras/números, convertendo para maiúsculas

            self.score_text(20, name, (255, 255, 255), (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 30))
            pygame.display.flip()

    def show_score(self):
        """Exibe a tela de pontuação."""
        db_proxy = DBProxy('game_scores.db')
        scores = db_proxy.retrieve_top10()
        self.window.fill((0, 0, 0))
        self.score_text(48, 'TOP 10 SCORES', (255, 255, 0), (WIN_WIDTH / 2, WIN_HEIGHT / 6))
        self.score_text(20, 'NAME     SCORE     DATE', (255, 255, 255), (WIN_WIDTH / 2, WIN_HEIGHT / 4))

        y_offset = WIN_HEIGHT / 3
        for player in scores:
            name, score, date = player[1], player[2], player[3]
            self.score_text(20, f'{name}    {score}   {date}', (255, 255, 255), (WIN_WIDTH / 2, y_offset))
            y_offset += 30

        self.score_text(18, 'Press ENTER to return', (255, 255, 255), (WIN_WIDTH / 2, WIN_HEIGHT - 50))
        pygame.display.flip()

        # Espera o jogador pressionar ENTER para sair
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Exibe um texto na tela."""
        font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    def get_formatted_date(self):
        """Retorna a data e hora formatada."""
        current_datetime = datetime.now()
        return current_datetime.strftime("%H:%M - %d/%m/%y")
