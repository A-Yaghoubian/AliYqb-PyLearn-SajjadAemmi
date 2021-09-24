import arcade

class Cloud(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.texture = arcade.load_texture('images\cloud.png')
        self.center_x = w
        self.center_y = h // 1.25
        self.speed = 1
        self.width = 60
        self.height = 30
        self.change_x = -1
    
    def move(self):
        self.center_x += self.change_x * self.speed