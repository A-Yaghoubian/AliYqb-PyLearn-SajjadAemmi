import random
import time
import arcade
from ground import Ground
from dino import Dino
from kaktos import Kaktos
from cloud import Cloud

class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 300
        super().__init__(self.w, self.h, 'Dino - Google Chrome Runner - Ali Yaghoubian')
        self.background_image = arcade.load_texture('images/background.png')
        self.ground = Ground(self.w, self.h)
        self.g = [self.ground]
        self.dino = Dino(self.w, self.h)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.g, gravity_constant=0.2)
        self.kaktos_list = []
        self.t1_kaktos = time.time()
        self.cloud_list = []
        self.t1_cloud = time.time()
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        self.dino.draw()
        self.ground.draw()
        for kaktos in self.kaktos_list:
            kaktos.draw()
        for cloud in self.cloud_list:
            cloud.draw()
        
    def on_update(self, delta_time: float):
        self.physics_engine.update()
        # self.dino.update_animation()
        
        dis_kaktos = random.randint(6, 10)
        if time.time() - self.t1_kaktos > dis_kaktos:
            self.kaktos_list.append(Kaktos(self.w, self.h))
            self.t1_kaktos = time.time()
        for kaktos in self.kaktos_list:
            kaktos.move()
        for i in range(len(self.kaktos_list)):
            try:
                if self.kaktos_list[i].center_x < 0:
                    self.kaktos_list.pop(i)
                    print('kaktos deleted!')
            except:
                pass
        
        dis_clouds = random.randint(6, 16)
        if time.time() - self.t1_cloud > dis_clouds:
            self.cloud_list.append(Cloud(self.w, self.h))
            self.t1_cloud = time.time()
        for cloud in self.cloud_list:
            cloud.move()
        for i in range(len(self.cloud_list)):
            try:
                if self.cloud_list[i].center_x < 0:
                    self.cloud_list.pop(i)
                    print('cloud deleted!')
            except:
                pass
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP and self.physics_engine.can_jump():
            self.dino.change_y = 10
        
game = Game()
arcade.run()