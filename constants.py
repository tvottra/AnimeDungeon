import pygame
from spritesheet import SpriteSheet
import setup_sprites
pygame.init()


GAME_WIDTH = 800
GAME_HEIGHT = 600

# Color Definitions
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

# Game colors

COLOR_DEFAULT_BG = COLOR_GREY

#SPRITES
#characters are 24x32
CHAR_WIDTH = 24
CHAR_HEIGHT = 32
SPRITESHEET_BACKGROUND = -1 #(49, 115, 116)

S_PLAYER = None
char_names = ["saffron", "pepper"]
paths = ["images/characters/" + x + ".png"for x in char_names]
char_paths = dict(zip(char_names, paths))
def initialize_sprites():
    #load up sprite frames and sprite surfaces
    global S_PLAYER
    saffron_frames = setup_sprites.make_sprite_frames(char_paths["saffron"])
    S_PLAYER = saffron_frames['L1']