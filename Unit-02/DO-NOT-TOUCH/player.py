import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load().convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()