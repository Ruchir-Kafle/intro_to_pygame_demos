import pygame
from globals.python_defaults import colors

class Button(pygame.sprite.Sprite):
    
    def __init__(self, size, coordinates, group, color, text, font):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((size["x"], size["y"]))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        
        self.rect.x = coordinates["x"]
        self.rect.y = coordinates["y"]
        
        self.text = font.render(text, True, colors.WHITE)
        
        self.text_rect = self.text.get_rect()

        self.text_rect.center = (self.rect.center[0], self.rect.center[1])

        self.image.blit(self.text, (self.text_rect.x, self.text_rect.y))

        group.add(self)