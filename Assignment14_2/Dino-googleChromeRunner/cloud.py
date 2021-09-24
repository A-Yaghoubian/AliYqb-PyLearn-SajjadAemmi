import random
import arcade

class Cloud(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.texture = arcade.load_texture('images\cloud.png')
        self.center_x = w
        r = random.choice([1.20, 1.25, 1.30])
        self.center_y = h // r
        s = random.choice([1, 1.5])
        self.speed = 1
        self.width = 60
        h = random.choice([25, 30, 35])
        self.height = h
        self.change_x = -1
    
    def move(self):
        self.center_x += self.change_x * self.speed