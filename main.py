import pygame
import time

from pygame.locals import *

# dictionary of color and corresponding RGB value
#   Example:
#           Color_map["red"] -> (255,0,0)
Color_map = {"red": (255, 0, 0),
             "gree": (0, 255, 0),
             "blue": (0, 0, 255),
             "black": (255, 255, 255),
             "white": (0, 0, 0)}


# function that prints text at designated pos
#   Input:
#           window: the window to display the text
#           txt: the text string that needs to be printed, default = "Hello"
#           x  : x coordinate of the top left of text box, default = 0
#           y  : y coordinate of the top left of text box, default = 0
#   Return:
#           None
def show_txt(window, txt="Hello", x=0, y=0):
    pygame.font.init()
    font = pygame.font.Font("freesansbold.ttf", 32)
    text_box = font.render(txt, True, Color_map["white"])
    window.blit(text_box, (x, y))
    return


# main function that creates the main game window
if __name__ == "__main__":
    pygame.init()
    board = pygame.display.set_mode((900, 900))
    board.fill(Color_map["black"])
    # need to update the screen using flip or update
    # flip: redraw
    # update: update on existing
    pygame.display.flip()

    # flag for exiting event loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    pass

    time.sleep(4)
