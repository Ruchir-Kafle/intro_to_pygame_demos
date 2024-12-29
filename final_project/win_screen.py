import pygame
from globals.python_defaults import colors
from final_project import button

class Win_Screen():
    def __init__(self, screen_size):
        button_group = pygame.sprite.Group()
        
        color = (*colors.BLACK, 50)

        self.screen = pygame.Surface((screen_size["x"], screen_size["y"]), pygame.SRCALPHA)
        self.screen.fill(color)

        a_button = button.Button(screen_size, {"x": 500, "y": 500}, {"x": 7, "y": 7}, button_group)

        print(a_button)
        
        button_group.draw(self.screen)