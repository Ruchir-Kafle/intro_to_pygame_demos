import pygame
from globals.python_defaults import colors
from final_project import button

class Win_Screen():
    def __init__(self, screen_size):
        button_group = pygame.sprite.Group()
        
        color = (*colors.BLACK, 50)

        self.screen = pygame.Surface((screen_size["x"], screen_size["y"]), pygame.SRCALPHA)
        self.screen.fill(color)

        a_button = button.Button(size={"x": 400, "y": 100}, coordinates={"x": 0, "y": 0}, group=button_group, color=colors.BLUE)
        
        button_group.draw(self.screen)