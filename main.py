import pygame
import time

from pygame.locals import *

# dictionary of color and corresponding RGB value
#   Key:
#       color name for pure colors : "red" for pure red
#       prefix d for dark colors   : "d_red" for dark red
#   Example:
#           Color_map["red"] -> (255,0,0)
Color_map = {"red": (255, 0, 0),
             "gree": (0, 255, 0),
             "d_green": (0, 133, 46),
             "blue": (0, 0, 255),
             "black": (0, 0, 0),
             "white": (255, 255, 255)}


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
    board.fill(Color_map["white"])
    # need to update the screen using flip or update
    # flip: update the whole screen
    # update: can update part of the screen or the whole screen
    pygame.display.flip()

    # flag for exiting event loop
    # Possible value:
    #               'R' : running
    #               'E' : end
    #               'I' : init(start a new game)
    run_sts = 'I'

    while run_sts != 'E':
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # if hit esc key, exit
                if event.key == K_ESCAPE:
                    run_sts = 'E'

                elif event.key == K_RETURN:
                    if run_sts == 'I':
                        run_sts == 'R'
            elif event.type == QUIT:
                run_sts = 'E'
    # remains: if the game end save the record to a text file
    time.sleep(4)
