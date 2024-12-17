import pygame

class Block(pygame.sprite.Sprite):
    
    def __init__(self, type_of_block, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("final_project/assets/background_block.webp").convert_alpha()
        self.type = type_of_block

        if self.type == 0:
            self.image = pygame.image.load("final_project/assets/background_block.webp").convert_alpha()
        elif self.type == 1:
            self.image = pygame.image.load("final_project/assets/basic_block.webp").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("final_project/assets/top_grid_block.webp").convert_alpha()
        elif self.type == 3:
            self.image = pygame.image.load("final_project/assets/under_grid_block.webp").convert_alpha()
        elif self.type == 4:
            self.image = pygame.image.load("final_project/assets/basic_spike.webp").convert_alpha()
        elif self.type == 5:
            self.image = pygame.image.load("final_project/assets/basic_thorns.webp").convert_alpha()            

        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()