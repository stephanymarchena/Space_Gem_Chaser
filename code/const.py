 # Constantes do jogo
import pygame

# C - Cores do Jogo
C_WHITE = (255, 255, 255)
C_CYAN = (8, 225, 138)
C_CYAN_2 = (191, 255, 229)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)


#E - velocidade das entidades

ENTITY_HEALTH = {
    'bg_1': 999,
    'bg_2': 999,
    'bg_3': 999,
    'bg_4': 999,
    'bg_5': 999,
    'astronaut_1': 300,
    'Player1Shot': 1,
    'enemy_1': 50,
    'enemy_1_damage': 1,
    'enemy_2': 60,
    'enemy_2_damage': 1,
    'enemy_5': 40,
    'enemy_5_damage': 1,
    'gem_1': 1,
    'gem_2': 1,
    'gem_3': 1,
    'gem_4': 1,

}



ENTITY_SPEED = {
    'bg_1': 0,
    'bg_2': 2,
    'bg_3': 3,
    'bg_4': 5,
    'bg_5': 4,
    'astronaut_1': 4,
    'enemy_1': 2,
    'enemy_2': 1,
    'enemy_5': 3,
    'gem_1': 1,
    'gem_2': 3,
    'gem_3': 2,
    'gem_4': 4,
}

# Gerando os inimigos
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_GEM = pygame.USEREVENT + 2


# M - Configuração do menu
MENU_OPTION = ('START GAME',
               'SCORE',
               'EXIT')


# P - Controles do astronauta
CONTROL_PLAYER_UP ={ 'astronaut_1': pygame.K_UP,}
CONTROL_PLAYER_DOWN = { 'astronaut_1': pygame.K_DOWN}

CONTROL_PLAYER_RIGHT = { 'astronaut_1': pygame.K_RIGHT}
CONTROL_PLAYER_LEFT = {'astronaut_1': pygame.K_LEFT}

# Espaçamento do HUD
PADDING = 20

#S
SPAWN_TIME = 1000
SPAWN_TIME_GEM = 2000

SPACING = 120  # Distância entre os textos superiores

# W - Configurações da tela
WIN_WIDTH = 800
WIN_HEIGHT = 600
FPS = 60




