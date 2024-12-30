import pygame

class Button(pygame.sprite.Sprite):
    
    def __init__(self, size, coordinates, group, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((size["x"], size["y"]))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        
        self.rect.x = coordinates["x"]
        self.rect.y = coordinates["y"]

        group.add(self)