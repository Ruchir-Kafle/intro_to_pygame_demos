import pygame

class Block(pygame.sprite.Sprite):
    
    def __init__(self, type_of_block, size, coordinates, group):
        pygame.sprite.Sprite.__init__(self)

        self.type = type_of_block

        if self.type == 0:
            self.image = pygame.image.load("final_project/assets/blocks/basic_spike.webp").convert_alpha()
        elif self.type == 1:
            self.image = pygame.image.load("final_project/assets/blocks/under_grid_block.webp").convert_alpha()
        elif self.type == 2:
            self.image = pygame.image.load("final_project/assets/blocks/background_block.webp").convert_alpha()
        elif self.type == 3:
            self.image = pygame.image.load("final_project/assets/blocks/GridBlock02.webp").convert_alpha()
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.type == 4:
            self.image = pygame.image.load("final_project/assets/blocks/top_grid_block.webp").convert_alpha()
        elif self.type == 5:
            self.image = pygame.image.load("final_project/assets/blocks/GridBlock03.webp").convert_alpha()
        elif self.type == 10:
            self.image = pygame.image.load("final_project/assets/blocks/GridBlock03.webp").convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.type == 13:
            self.image = pygame.image.load("final_project/assets/blocks/basic_block.webp").convert_alpha()
        elif self.type == 14:
            self.image = pygame.image.load("final_project/assets/blocks/GridBlock02.webp").convert_alpha()
        elif self.type == 15:
            self.image = pygame.image.load("final_project/assets/blocks/GridBlock02.webp").convert_alpha()
            self.image = pygame.transform.rotate(self.image, 90)
        else:
            self.image = pygame.image.load("final_project/assets/blocks/basic_thorns.webp").convert_alpha()


        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.initial_x = coordinates["x"]
        
        self.rect.x = self.initial_x
        self.rect.bottom = coordinates["y"]

        group.add(self)