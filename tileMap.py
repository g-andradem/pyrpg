class TileMap:
    def __init__(self, title_size = 16):
        self.title_size = title_size
        self.tilemap = {}
        self.offgrid_tiles = []