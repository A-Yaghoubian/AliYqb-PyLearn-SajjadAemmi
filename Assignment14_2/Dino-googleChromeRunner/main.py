import random
import time
import arcade
from ground import Ground
from dino import Dino
from kaktos import Kaktos
from cloud import Cloud
from bird import Bird

def highScore():
    f = open('high.txt', 'r')
    highscore = f.read()
    f.close()
    return highscore   

def saving(ex_score, now_score):
    f = open('high.txt', 'w')
    if int(ex_score) >= int(now_score):
        f.write(str(ex_score))
    else:
        f.write(str(now_score))
    f.close()

class Game(arcade.Window):
    def __init__(self):
        self.w = 900
        self.h = 300
        super().__init__(self.w, self.h, 'Dino - Google Chrome Runner - Ali Yaghoubian')
        self.background_image = arcade.load_texture('images/background.png')
        self.t1_background = time.time()
        self.ground = Ground(self.w, self.h)
        self.g = arcade.SpriteList()
        self.g.append(self.ground)
        self.dino = Dino(self.w, self.h)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.g, gravity_constant=0.5)
        self.bird_list = arcade.SpriteList()
        self.t1_bird = time.time()
        self.kaktos_list = arcade.SpriteList()
        self.t1_kaktos = time.time()
        self.cloud_list = arcade.SpriteList()
        self.t1_cloud = time.time()
        self.t1_score = time.time()
        self.gameover = False
        self.highscore = highScore()
        self.jump_sound = 'sounds/jump.mp3'
        self.die_sound = 'sounds/die.mp3'
        self.checkPoint_sound = 'sounds/checkPoint.mp3'
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        arcade.draw_text('Record', 700, 280, arcade.color.RED, font_name='Kenney Mini Square')
        arcade.draw_text(str(self.highscore), 780, 280, arcade.color.RED, font_name='Kenney Mini Square')
        arcade.draw_text(str(self.dino.score), 820, 280, arcade.color.RED, font_name='Kenney Mini Square')
        self.dino.draw()
        self.ground.draw()
        for kaktos in self.kaktos_list:
            kaktos.draw()
        for cloud in self.cloud_list:
            cloud.draw()
        for bird in self.bird_list:
            bird.draw()
        
        if self.gameover == True:
            arcade.draw_text('Game Over', self.w // 2, self.h // 2, arcade.color.RED, font_name='Kenney Mini Square')
            arcade.Sound(self.die_sound).play()
            arcade.finish_render()
            time.sleep(3)
            saving(self.highscore, self.dino.score)
            arcade.exit()
        
    def on_update(self, delta_time: float):
        self.physics_engine.update()
        # self.dino.update_animation()
        for bird in self.bird_list:
            bird.update_animation()
        
        if time.time() - self.t1_background > 10:
            if self.background_image == arcade.load_texture('images/background.png'):
                self.background_image = arcade.load_texture('images/dark_background.png')
            elif self.background_image == arcade.load_texture('images/dark_background.png'):
                self.background_image = arcade.load_texture('images/background.png')
            self.t1_background = time.time()
        
        if self.dino.score > 500:
            dis_bird = random.randint(10, 20)
            if time.time() - self.t1_bird > dis_bird:
                self.bird_list.append(Bird(self.w, self.h))
                self.t1_bird = time.time()
            for bird in self.bird_list:
                bird.move()
            for i in range(len(self.bird_list)):
                try:
                    if self.bird_list[i].center_x < 0:
                        self.bird_list.pop(i)
                except:
                    pass
        
        dis_kaktos = random.randint(6, 10)
        if time.time() - self.t1_kaktos > dis_kaktos:
            if self.dino.score <= 250:
                self.kaktos_list.append(Kaktos(self.w, self.h, 3.5))
            elif 500 >= self.dino.score > 250:
                self.kaktos_list.append(Kaktos(self.w, self.h, 4.5))
            elif 1000 >= self.dino.score > 500:
                self.kaktos_list.append(Kaktos(self.w, self.h, 6))
            elif self.dino.score > 1000:
                self.kaktos_list.append(Kaktos(self.w, self.h, 8))
            self.t1_kaktos = time.time()
        for kaktos in self.kaktos_list:
            kaktos.move()
        for i in range(len(self.kaktos_list)):
            try:
                if self.kaktos_list[i].center_x < 0:
                    self.kaktos_list.pop(i)
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
            except:
                pass
            
        if time.time() - self.t1_score > 0.1:
            self.dino.score += 1
            self.t1_score = time.time()
            
        if self.dino.score % 100 == 0 and self.dino.score != 0:
            arcade.Sound(self.checkPoint_sound).play()
            
        for kaktos in self.kaktos_list:
            try:
                if arcade.check_for_collision(self.dino, kaktos):
                    self.gameover = True
            except:
                pass
        
        for bird in self.bird_list:
            try:
                if arcade.check_for_collision(self.dino, bird):
                    self.gameover = True
            except:
                pass
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.dino.change_y = 13
                arcade.Sound(self.jump_sound).play()
        
        if key == arcade.key.DOWN:
            self.dino.texture = arcade.load_texture('images\down_1.png')
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.DOWN:
            self.dino.texture = arcade.load_texture('images\jump.png')
        
game = Game()
arcade.run()