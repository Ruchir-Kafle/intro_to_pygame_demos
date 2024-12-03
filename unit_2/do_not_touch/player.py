import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load("character-sprite.png").convert()
        img = pygame.transform.scale(img, (99, 57))

        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.acceleration_due_to_gravity = 0.1
        self.current_gravity = 0

    def apply_gravity(self, screen_size):
        if self.rect.y + self.current_gravity <= screen_size:
            self.current_gravity += self.acceleration_due_to_gravity
        else:
            self.current_gravity = 0

        self.rect.y += self.current_gravity

    def jump(self, screen_size):
        if self.rect.y == screen_size:
            self.rect.y

    # def run(self):
