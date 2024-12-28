import pygame
from globals.python_defaults import colors
from final_project import button

class Win_Screen():
    def __init__(self, screen_size):
        color = (*colors.BLACK, 50)

        self.screen = pygame.Surface((screen_size["x"], screen_size["y"]), pygame.SRCALPHA)
        self.screen.fill(color)

        a_button = button.Button(screen_size)
        self.screen.blit(a_button.screen, (500, 500))