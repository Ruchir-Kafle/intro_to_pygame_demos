from final_project import block
from final_project import tilemap_render

class Map():
    def __init__(self, tile_size, screen_size, tile_group):
        
        self.tile_size = tile_size
        self.screen_size = screen_size

        self.tilemap = tilemap_render.TileMap()

        # self.longest = 0
        self.farthest = 0
        self.start_position = self.tile_size["x"] * 10

        # for level in self.tilemap.levels:        
        #     self.longest = max(len(self.tilemap.levels[level]), self.longest)

        self.create_map(tile_group)

    def create_map(self, tile_group):
        
        for level in self.tilemap.levels:

            for tile_object in self.tilemap.levels[level]:
                
                # if tile_object == "x":

                #     pass

                #     # if previous_image == 0:
                #     #     continue

                #     # print(previous_image)
                    
                #     # iterations = longest
                #     # start_position = self.tile_size["x"] * 10
                    
                #     # for filler_tile in range(count, iterations):
                #     #     map_tile = block.Block(previous_image, (self.tile_size["x"], self.tile_size["y"]))
                #     #     map_tile.rect.x = (filler_tile * (self.tile_size["x"])) + start_position
                #     #     map_tile.rect.bottom = self.screen_size["y"] - level * (self.tile_size["y"])

                #     #     if previous_image == 0:
                #     #         background_group.add(map_tile)
                #     #     else:
                #     #         tile_group.add(map_tile)

                # else:

                start_position = self.tile_size["x"] * 20

                map_tile = block.Block(tile_object["id"], (self.tile_size["x"], self.tile_size["y"]))
                map_tile.rect.x = (tile_object["x"] * (self.tile_size["x"])) + start_position
                map_tile.initial_x = (tile_object["x"] * (self.tile_size["x"])) + start_position
                map_tile.rect.bottom = (level + 1) * (self.tile_size["y"]) + (((self.screen_size["y"] // self.tile_size["y"]) - (max(self.tilemap.levels.keys()) + 1)) * self.tile_size["y"])

                self.farthest = map_tile.rect.x

                tile_group.add(map_tile)
