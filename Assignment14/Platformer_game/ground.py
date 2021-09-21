import arcade

class Ground(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grassMid.png')
        self.center_x = w
        self.center_y = h
        self.width = 130
        self.height = 130
        
class Box(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.texture = arcade.load_texture(':resources:images/tiles/grassHalf_mid.png')
        self.center_x = w
        self.center_y = h
        self.width = 120
        self.height = 120