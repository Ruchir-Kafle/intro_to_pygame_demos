import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_x):
        pygame.sprite.Sprite.__init__(self)
        
        self.player(False, screen_x)

        self.acceleration_due_to_gravity = 0.25
        self.current_gravity = 0

        self.jump_increment = 10
        self.jump_decrement = 0.25
        self.current_jump = 0
        self.apply_jump = False

        self.walk_speed = 5

    def player(self, direction, screen_x):
        self.images = []

        self.player_scale = {"x": 99, "y": 57}
        
        try:
            if self.rect:
                self.store_x = self.rect.x
                self.store_y = self.rect.y
        except AttributeError:
            self.store_x = (screen_x - self.player_scale.x) / 2
            self.store_y = 0
        
        self.img = pygame.image.load("globals/assets/character-sprite.png").convert()
        self.img = pygame.transform.scale(self.img, self.player_scale)
        self.img = pygame.transform.flip(self.img, direction, False)

        self.images.append(self.img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.rect.x = self.store_x
        self.rect.y = self.store_y

    def apply_gravity(self, screen_y):
        if not self.apply_jump:
            if self.rect.y + self.current_gravity < screen_y - self.player_scale[1]:
                self.current_gravity += self.acceleration_due_to_gravity
            else:
                self.current_gravity = 0

            self.rect.y += self.current_gravity

    def jump(self, screen_y, jumping):
        if jumping:
            if self.rect.y + self.current_gravity == screen_y - self.player_scale[1]:
                self.apply_jump = True
                self.current_jump = self.jump_increment
                self.current_gravity = 0

        if self.apply_jump:
            if self.current_jump >= self.jump_decrement:
                self.current_jump -= self.jump_decrement
            else:
                self.apply_jump = False
                self.current_jump = 0

        self.rect.y -= self.current_jump

    def walk(self, direction, screen_x, screen_y):
        self.rect.x += (direction * self.walk_speed)
    
    def user_input_process(self, pressed, screen_x, screen_y):
        if pressed[pygame.K_a]:
            self.walk(-1, screen_x, screen_y)
            self.player(True, screen_x)

        if pressed[pygame.K_d]:
            self.walk(1, screen_x, screen_y)
            self.player(False, screen_x)

        if pressed[pygame.K_SPACE]:
            self.jump(screen_y, True)

    def run(self, screen_y):
        self.apply_gravity(screen_y)
        self.jump(screen_y, False)