from final_project import block
from final_project import tilemap_reformat

class Map():
    def __init__(self, tile_size, screen_size, tile_group):
        
        self.tile_size = tile_size
        self.screen_size = screen_size

        self.tilemap = tilemap_reformat.TileMap()

        self.farthest = 0
        self.start_position = self.tile_size["x"] * 10

        self.create_map(tile_group)

    def create_map(self, tile_group):
        
        for level in self.tilemap.levels:

            for tile_object in self.tilemap.levels[level]:
                
                start_position = self.tile_size["x"] * 20

                map_tile_x = (tile_object["x"] * (self.tile_size["x"])) + start_position
                map_tile_y = (level + 1) * (self.tile_size["y"]) + (((self.screen_size["y"] // self.tile_size["y"]) - (max(self.tilemap.levels.keys()) + 1)) * self.tile_size["y"])
                
                map_tile = block.Block(tile_object["id"], (self.tile_size["x"], self.tile_size["y"]), {"x": map_tile_x, "y": map_tile_y})

                self.farthest = max(self.farthest, map_tile.rect.x)

                tile_group.add(map_tile)
