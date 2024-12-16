class Map():
    def __init__(self, screen_size, tile_size):
        self.levels = {
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            1: [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            0: [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1]
        }

        for level in range(len(self.levels), screen_size["y"] // tile_size["y"]):
            self.levels[level] = [0]
