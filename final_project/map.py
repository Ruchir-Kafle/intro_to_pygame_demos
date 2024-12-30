import pygame
from final_project import block
from final_project import tilemap_reformat

class Map():
    def __init__(self, tile_size, screen_size):
        self.tile_group = pygame.sprite.Group()
        
        self.tile_size = tile_size
        self.screen_size = screen_size

        self.tilemap = tilemap_reformat.TileMap()

        self.farthest = 0
        self.start_position = self.tile_size["x"] * 30

        self.create_map()

    def create_map(self):
        
        for level in self.tilemap.levels:

            for tile_object in self.tilemap.levels[level]:
                
                map_tile_x = (tile_object["x"] * (self.tile_size["x"])) + self.start_position
                map_tile_y = (level + 1) * (self.tile_size["y"]) + (((self.screen_size["y"] // self.tile_size["y"]) - (max(self.tilemap.levels.keys()) + 1)) * self.tile_size["y"])
                
                map_tile = block.Block(type_of_block=tile_object["id"], size=(self.tile_size["x"], self.tile_size["y"]), coordinates={"x": map_tile_x, "y": map_tile_y}, group=self.tile_group)

                self.farthest = max(self.farthest, map_tile.rect.x)

    def update_map(self, player):
        for block in self.tile_group:
            block.rect.x = block.initial_x - player.player_offset