import pygame
import tcod

#game files
import constants

def draw_game():
    global SURFACE_MAIN

    # Clear the surface
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)
    # TODO draw the map

    # Draw the protagonist
    SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200)) #draw the player at 200,200

    #update the display: use flip
    pygame.display.flip()

def game_main_loop():
    """The main game will be looped until a quit condition is met
    """
    game_quit = False

    while not game_quit:
        #TODO get player input
        events_list = pygame.event.get()

        #TODO process input
        for event in events_list:
            if event.type == pygame.QUIT:
                game_quit = True
        draw_game()

    pygame.quit()
    exit()

def game_initialize():
    """Initialize the main window and pygame"""
    global SURFACE_MAIN #global vars will be all caps
    # init pygame
    pygame.init()
    SURFACE_MAIN = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT))
    constants.initialize_sprites()

if __name__ == '__main__':
    game_initialize()
    game_main_loop()