class Map():
    def __init__(self, screen_size, tile_size):
        self.levels = {
            2: ["x", 0, "x"],
            1: ["x", 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            0: ["x", 1, "x"]
        }

        for level in range(len(self.levels), screen_size["y"] // tile_size["y"]):
            self.levels[level] = ["x", 0, "x"]
