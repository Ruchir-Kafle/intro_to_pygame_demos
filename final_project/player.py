import pygame
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.screen_size = screen_size
        self.tile_size = tile_size
        self.initial_coordinates = {"x": self.tile_size["x"] * 10, "y": self.screen_size["y"]}

        self.started = False
        self.is_dead = False
        self.should_jump = False

        self.player_offset = 0
        self.walk_speed = 6.25

        self.floor = self.screen_size["y"]
        self.velocity_y = 0
        self.acceleration_due_to_gravity = 1
        self.jump_maximum = 11

        self.previous_time = time.time()

        self.instantiate_player()

    def instantiate_player(self):
        self.images = []

        self.img = pygame.image.load("final_project/assets/player.webp").convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.tile_size["x"], self.tile_size["y"]))

        self.images.append(self.img)
        self.image = self.images[0]

        self.player_scale = {"x": self.image.get_width(), "y": self.image.get_height()}

        try:
            if self.rect:
                self.store_x = self.rect.x
                self.store_y = self.rect.y
        except AttributeError:
            self.store_x = self.initial_coordinates["x"]
            self.store_y = self.initial_coordinates["y"]

        self.rect = self.image.get_rect()

        self.rect.x = self.store_x

        self.rect.bottom = self.store_y
        
    def apply_gravity(self):
        if self.rect.bottom + self.velocity_y < self.floor:
            self.velocity_y += self.acceleration_due_to_gravity
        else:
            self.velocity_y = 0
            self.rect.bottom = self.floor

        self.rect.y += self.velocity_y * (self.delta_time / 1.5)

    def jump(self):
        if self.started:
            if self.rect.bottom == self.floor:
                self.velocity_y = -1 * self.jump_maximum * (1.5)
        else:
            self.started = True

        self.should_jump = False

    def walk(self, direction):
        if self.started:
            self.player_offset += (direction * self.walk_speed) * (self.delta_time / 0.9)
    
    def process_user_input(self, pressed):
        if pressed[pygame.K_SPACE] or pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.should_jump = True

    def check_collisions(self, collisions):
        if collisions:

            for block in collisions:
                if block.type == 0:

                    self.floor = self.screen_size["y"]

                    if self.rect.center[1] >= block.rect.center[1]:
                        if self.rect.right > block.rect.left + 10 or self.rect.left < block.rect.right - 10:
                            self.trigger_death()
                else:
                    if self.rect.top >= block.rect.top:
                        self.trigger_death()
                    else:
                        self.floor = min(collision_object.rect.top for collision_object in collisions) + 1

                        if self.rect.bottom > self.floor:
                            self.rect.bottom = self.floor
        else:
            self.floor = self.screen_size["y"]

    def trigger_death(self):
        self.is_dead = True

        time.sleep(0.5)

        self.spawn()

    def spawn(self):
        self.player_offset = 0
        self.rect.bottom = self.initial_coordinates["y"]

        self.floor = self.screen_size["y"]

        self.is_dead = False

    def run(self, collisions):

        if not self.is_dead:  
            self.delta_time = (time.time() - self.previous_time) * 60
            self.previous_time = time.time()

            if self.should_jump:
                self.jump()

            self.walk(direction=1)

            self.apply_gravity()
            self.check_collisions(collisions=collisions)
