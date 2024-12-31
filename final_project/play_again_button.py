import pygame
from globals.python_defaults import colors

class Play_Again_Button(pygame.sprite.Sprite):
    
    def __init__(self, size, coordinates, group, color, text, font):
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.coordinates = coordinates
        self.color = color
        self.text = text
        self.font = font
        self.hovering = False

        self.create_background()

        self.create_text()

        group.add(self)

    def create_background(self):
        self.image = pygame.Surface((self.size["x"], self.size["y"]))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        
        self.rect.x = self.coordinates["x"]
        self.rect.y = self.coordinates["y"]

    def create_text(self):
        self.text = self.font.render(self.text, True, colors.WHITE)
        
        self.text_rect = self.text.get_rect()

        self.text_rect.center = (self.rect.center[0], self.rect.center[1])

        self.image.blit(self.text, (self.text_rect.x, self.text_rect.y))

    def hover(self, clicked=False, player=None):
        mouse_position = pygame.mouse.get_pos()
        all_x = range(self.rect.left, self.rect.right + 1)
        all_y = range(self.rect.top, self.rect.bottom + 1)

        if mouse_position[0] in all_x:
            if mouse_position[1] in all_y:
                self.hovering = True
                self.image.fill(colors.DARK_BLUE)
                self.image.blit(self.text, (self.text_rect.x, self.text_rect.y))

                if clicked:
                    player.spawn()

                    return True

                return False
        
        self.hovering = False
        self.image.fill(colors.BLUE)
        self.image.blit(self.text, (self.text_rect.x, self.text_rect.y))
