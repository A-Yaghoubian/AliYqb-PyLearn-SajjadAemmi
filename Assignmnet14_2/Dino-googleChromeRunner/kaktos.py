import random
import arcade

class Kaktos(arcade.Sprite):
    def __init__(self, w, h, s):
        super().__init__()
        mode = random.randint(0, 2)
        if mode == 0:
            self.texture = arcade.load_texture('images\kaktos_1.png')
        elif mode == 1:
            self.texture = arcade.load_texture('images\kaktos2.png')
        elif mode == 2:
            self.texture = arcade.load_texture('images\kaktos3.png')
        self.center_x = w
        self.center_y = h // 3 - 45
        self.speed = s
        self.width = 35
        self.height = 45
        self.change_x = -1
    
    def move(self):
        self.center_x += self.change_x * self.speed
        