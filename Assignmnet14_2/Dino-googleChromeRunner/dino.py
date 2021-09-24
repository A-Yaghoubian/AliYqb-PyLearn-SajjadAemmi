import arcade

class Dino(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__()
        # self.stand_right_textures = [arcade.load_texture('images/jump.png')]
        # self.walk_right_textures = [arcade.load_texture('images/walk1.png'),
        #                             arcade.load_texture('images/walk2.png')]
        # self.walk_down_textures = [arcade.load_texture('images/down1.png'),
        #                             arcade.load_texture('images/down2.png')]
        # self.walk_up_textures = [arcade.load_texture('images/jump.png')]
        
        # self.stand_right_textures = [arcade.load_texture('images/dino.png')]
        # self.walk_right_textures = [arcade.load_texture('images/walk0.png'), arcade.load_texture('images/walk1.png')]
        # self.walk_down_textures = [arcade.load_texture('images/down0.png'), arcade.load_texture('images/down0.png')]
        # self.walk_up_textures = [arcade.load_texture('images/dino.png')]
        
        self.texture = arcade.load_texture('images\jump.png')
        
        self.center_x = 65
        self.center_y = h // 3
        self.width = 55
        self.height = 75
        self.speed = 4
        self.score = 0
        