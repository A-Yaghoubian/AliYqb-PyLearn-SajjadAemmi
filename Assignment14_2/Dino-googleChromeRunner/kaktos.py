import random
import arcade

class Kaktos(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        mode = random.randint(0, 2)
        if mode == 0:
            self.texture = arcade.load_texture('images\kaktos1.png')
        elif mode == 1:
            self.texture = arcade.load_texture('images\kaktos2.png')
        elif mode == 2:
            self.texture = arcade.load_texture('images\kaktos3.png')
        self.center_x = w
        self.center_y = h // 3 - 20
        self.speed = 2
        self.width = 45
        self.height = 65
        self.change_x = -1
    
    def move(self):
        self.center_x += self.change_x * self.speed
        