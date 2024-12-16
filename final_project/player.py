import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.player(tile_size)

        self.floor = screen_size["y"]

        self.velocity_y = 0
        
        self.acceleration_due_to_gravity = 0.75

        self.applying_jump = False
        self.jump_maximum = 10

        self.walk_speed = 5

    def player(self, tile_size):
        self.images = []

        self.img = pygame.image.load("final_project/assets/player.webp").convert_alpha()
        self.img = pygame.transform.scale(self.img, (tile_size["x"], tile_size["y"]))

        self.images.append(self.img)
        self.image = self.images[0]

        self.player_scale = {"x": self.image.get_width(), "y": self.image.get_height()}

        try:
            if self.rect:
                self.store_x = self.rect.x
                self.store_y = self.rect.y
        except AttributeError:
            self.store_x = tile_size["x"]
            self.store_y = 0

        self.rect = self.image.get_rect()

        self.rect.x = self.store_x
        self.rect.y = self.store_y

    def apply_gravity(self):
        if self.rect.bottom + self.velocity_y < self.floor:
            self.velocity_y += self.acceleration_due_to_gravity
        else:
            self.velocity_y = 0
            self.rect.bottom = self.floor

        self.rect.y += self.velocity_y

    def jump(self):
        if self.rect.bottom == self.floor:
            self.applying_jump = True
            self.velocity_y = -1 * self.jump_maximum

    def walk(self, direction):
        self.rect.x += (direction * self.walk_speed)
    
    def process_user_input(self, pressed):
        if pressed[pygame.K_SPACE] or pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.jump()
        
        if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.walk(1)
        
        if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            self.walk(-1)

    def check_collisions(self, collisions, screen_size):
        if collisions:
            self.floor = max(collision_object.rect.top for collision_object in collisions) + 1

            if not self.applying_jump:
                self.rect.bottom = self.floor
        else:
            self.floor = screen_size["y"]

    def run(self, collisions, screen_size):
        # self.walk(0)
        self.apply_gravity()
        self.check_collisions(collisions, screen_size)