import json

class TileMap():
    def __init__(self):

        self.tile_objects = []

        with open("final_project/assets/tilemap.json", "r") as tilemap:
            content = json.load(tilemap)
            self.tile_objects = content["objects"]

        self.levels = {}

        for tile_object in self.tile_objects:
            all_levels = self.levels.keys()
            level = tile_object["y"]

            if level in all_levels:
                self.levels[level].append({"x": tile_object["x"], "id": tile_object["t"]["id"]})
            else:
                self.levels[level] = [{"x": tile_object["x"], "id": tile_object["t"]["id"]}]
