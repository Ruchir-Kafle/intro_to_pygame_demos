import pygame
from globals.python_defaults import colors

class Button(pygame.sprite.Sprite):
    def __init__(self, screen_size, size_divisor, coordinates):
        self.screen = pygame.Surface((screen_size["x"] / size_divisor["x"], screen_size["y"] / size_divisor["y"]), pygame.SRCALPHA)
        self.screen.fill(colors.BLUE)
        
        self.rect = self.screen.get_rect()        
        self.rect.x = coordinates["x"]
        self.rect.bottom = coordinates["y"]
