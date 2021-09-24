import random
import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self, w, h):
        super().__init__()
        # self.stand_left_textures = [()]
        self.walk_left_textures = [arcade.load_texture('images/bird_1.png'),
                                   arcade.load_texture('images/bird_2.png')]
        self.center_x = w
        self.center_y = h // 2 - 22
        self.speed = 3
        self.width = 20
        self.height = 30
        self.change_x = -1
    
    def move(self):
        self.center_x += self.change_x * self.speed
        