import pygame
from spritesheet import SpriteSheet
import constants

pygame.init()
orientations = ("U", "R", "D","L");
stages = (0, 1, 2) #1 is neutral


def make_sprite_frames(filename):
    """Returns a dictionary of sprites"""
    ss = SpriteSheet(filename)
    rects = []
    for i in range(len(orientations)):
        for j in range(len(stages)):
            rects.append((constants.CHAR_WIDTH * j,constants.CHAR_HEIGHT * i, constants.CHAR_WIDTH, constants.CHAR_HEIGHT))

    sprites = ss.images_at(*rects, colorkey=-1)
    framenames = [x + str(y) for x in orientations for y in stages]
    d = dict(zip(framenames, sprites))
    return d

