# Define as constantes do jogo
import pygame
from pygame import CONTROLLER_BUTTON_Y

# C - Cores do Jogo
C_WHITE = (255, 255, 255)
C_CYAN = (8, 225, 138)
C_CYAN_2 = (191, 255, 229)
C_BLACK = (0, 0, 0)


#E - velocidade das entidades
ENTITY_SPEED = {
    'bg_1': 0,
    'bg_2': 2,
    'bg_3': 3,
    'bg_4': 5,
    'bg_5': 4,
    'astronaut_1': 4,
    'enemy_1': 2,
    'enemy_2': 1,
    'enemy_3': 3,
    'enemy_4': 2,
    'enemy_5': 3,
    'enemy_6': 4,
    'enemy_7': 4,
    'enemy_8': 4,
    'enemy_9': 4,
}

# E - Gerando os inimigos
EVENT_ENEMY = pygame.USEREVENT + 1


# M - Configuração do menu
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')

# P - Controles do astronauta
CONTROL_PLAYER_UP ={ 'astronaut_1': pygame.K_UP,}
CONTROL_PLAYER_DOWN = { 'astronaut_1': pygame.K_DOWN}

CONTROL_PLAYER_RIGHT = { 'astronaut_1': pygame.K_RIGHT}
CONTROL_PLAYER_LEFT = {'astronaut_1': pygame.K_LEFT}


SPAWN_TIME = 5000

# W - Configurações da tela
WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 60




