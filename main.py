import pygame
import time

if __name__ == "__main__":
    pygame.init()
    board = pygame.display.set_mode((900, 900))
    board.fill((255, 255, 255))
    # need to update the screen using flip or update
    # flip: redraw
    # update: update on existing
    pygame.display.flip()

    # flag for exiting event loop

    time.sleep(4)