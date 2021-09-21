import arcade

class Star(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(':resources:images/items/star.png')
        self.center_x = w
        self.center_y = h
        self.width = 50
        self.height = 50