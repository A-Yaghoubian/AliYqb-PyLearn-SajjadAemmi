import random
import arcade
from arcade.texture import load_texture

class Enemy(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        # self.texture = arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')
        self.stand_right_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png')]
        self.stand_left_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_idle.png', mirrored=True)]
        self.walk_right_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk0.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk1.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk2.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk3.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk4.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk5.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk6.png'),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk7.png')]
        self.walk_left_textures = [arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk0.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk1.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk2.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk3.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk4.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk5.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk6.png', mirrored=True),
                                    arcade.load_texture(':resources:images/animated_characters/zombie/zombie_walk7.png', mirrored=True)]
        self.center_x = random.randint(100, 900)
        self.center_y = 1000
        self.width = 80
        self.height = 120     
        self.change_x = random.choice([-1, 1])
        self.speed = 2
        