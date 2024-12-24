import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, tile_size, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.screen_size = screen_size
        self.tile_size = tile_size
        self.initial_coordinates = {"x": self.tile_size["x"] * 10, "y": self.screen_size["y"]}

        self.player_offset = 0

        self.floor = self.screen_size["y"]

        self.velocity_y = 0
        
        self.acceleration_due_to_gravity = 0.75

        self.jump_maximum = 11

        self.walk_speed = 5

        self.player()

        self.previous_frame = {"x": self.player_offset, "y": self.initial_coordinates["y"]}

    def player(self):
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

        self.rect.y += self.velocity_y

    def jump(self):
        if self.rect.bottom == self.floor:
            self.velocity_y = -1 * self.jump_maximum

    def walk(self, direction):
        self.player_offset += (direction * self.walk_speed)
    
    def process_user_input(self, pressed):
        if pressed[pygame.K_SPACE] or pressed[pygame.K_w] or pressed[pygame.K_UP]:
            self.jump()
        
        # if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        #     self.walk(1)
        
        # if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        #     self.walk(-1)

    def check_collisions(self, collisions):
        if collisions:

            for block in collisions:
                if block.type == 0:

                    self.floor = self.screen_size["y"]

                    if self.rect.center[1] >= block.rect.center[1]:
                        self.trigger_death()
                else:

                    horizontal = self.player_offset - self.previous_frame["x"]

                    if self.rect.y > block.rect.top:
                        if horizontal > 0:
                            self.player_offset = block.rect.left
                        elif horizontal < 0:
                            self.player_offset = block.rect.right
                    else:
                        self.floor = min(collision_object.rect.top for collision_object in collisions) + 1

                        if self.rect.bottom > self.floor:
                            self.rect.bottom = self.floor
        else:
            self.floor = self.screen_size["y"]

    def trigger_death(self):
        self.player_offset = 0
        self.rect.bottom = self.initial_coordinates["y"]

        self.floor = self.screen_size["y"]

    def check_out_of_bounds(self, map):
        if self.player_offset >= map.farthest:
            self.trigger_death()

    def run(self, collisions, map):
        self.previous_frame = {"x": self.player_offset, "y": self.rect.y}

        self.walk(1)
        self.apply_gravity()
        self.check_collisions(collisions)
        self.check_out_of_bounds(map)
