class Map():
    def __init__(self, screen_size, tile_size):
        self.levels = {
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            1: [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 3],
            0: [0, 1, 0, 4, 2, 4, 4, 2, 4, 4, 2, 4, 2]
        }

        for level in range(len(self.levels), screen_size["y"] // tile_size["y"]):
            self.levels[level] = [0]
