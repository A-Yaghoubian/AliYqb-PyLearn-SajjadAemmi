import arcade

class Ground(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.texture = arcade.load_texture('images\ground.png')
        self.center_x = w // 2
        self.center_y = h // 20
        self.width = w
        self.height = h // 3