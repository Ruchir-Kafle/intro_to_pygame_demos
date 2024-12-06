import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.player(False, screen_size)

        self.acceleration_due_to_gravity = 0.25
        self.current_gravity = 0

        self.jump_increment = 10
        self.jump_decrement = 0.25
        self.current_jump = 0
        self.apply_jump = False

        self.walk_speed = 5

    def player(self, direction, screen_size):
        self.images = []

        self.img = pygame.image.load("globals/assets/character-sprite.png").convert_alpha()
        self.img = pygame.transform.scale_by(self.img, 1/3)
        self.img = pygame.transform.flip(self.img, direction, False)

        self.images.append(self.img)
        self.image = self.images[0]

        self.player_scale = {"x": self.image.get_width(), "y": self.image.get_height()}

        try:
            if self.rect:
                self.store_x = self.rect.x
                self.store_y = self.rect.y
        except AttributeError:
            self.store_x = (screen_size["x"] - self.player_scale["x"]) / 2
            self.store_y = 0

        self.rect = self.image.get_rect()

        self.rect.x = self.store_x
        self.rect.y = self.store_y

    def apply_gravity(self, screen_size):
        if not self.apply_jump:
            if self.rect.y + self.current_gravity < screen_size["y"] - self.player_scale["y"]:
                self.current_gravity += self.acceleration_due_to_gravity
            else:
                self.current_gravity = 0

            self.rect.y += self.current_gravity

    def jump(self, screen_size, jumping):
        if jumping:
            if self.rect.y + self.current_gravity == screen_size["y"] - self.player_scale["y"]:
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

    def walk(self, direction, screen_size):
        self.rect.x += (direction * self.walk_speed)
    
    def user_input_process(self, pressed, screen_size):
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.walk(-1, screen_size)
            self.player(True, screen_size)

        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.walk(1, screen_size)
            self.player(False, screen_size)

        if pressed[pygame.K_SPACE] or pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.jump(screen_size, True)

    def run(self, screen_size):
        self.apply_gravity(screen_size)
        self.jump(screen_size, False)