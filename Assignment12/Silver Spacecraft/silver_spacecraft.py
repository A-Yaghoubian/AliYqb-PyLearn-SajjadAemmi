import math
import time
import random
import arcade

class Star(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(':resources:images/items/star.png')
        self.center_x = w + 20
        self.center_y = h + 20
        self.width = 30
        self.height = 30

class Explosion(arcade.Sprite):
    def __init__(self, x, y, time):
        super().__init__(':resources:images/topdown_tanks/treeBrown_small.png')
        self.center_x = x
        self.center_y = y
        self.width = 40
        self.height = 40
        self.time = time

class Enemy(arcade.Sprite):
    def __init__(self, w, h, speed):
        super().__init__(':resources:images/space_shooter/playerShip2_orange.png')
        self.angle = 180
        self.speed = speed
        self.center_x = random.randint(0, w)
        self.center_y = h
        self.width = 36
        self.height = 36
    
    def move(self):
        self.center_y -= self.speed

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
        
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)
        
class SpaceCraft(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(filename=':resources:images/space_shooter/playerShip1_green.png')
        self.width = 48
        self.height = 48
        self.center_x = w // 2
        self.center_y = 40
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 3
           
    def rotate(self):
        self.angle += self.change_angle * self.speed
        
    def fire(self, sound):
        self.bullet_list.append(Bullet(self))
        arcade.Sound(sound).play()

class Game(arcade.Window):
    def __init__(self):
        self.w = 600
        self.h = 500
        super().__init__(self.w, self.h, 'Silver SpaceCraft')
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.gameover_background_image = arcade.load_texture(':resources:onscreen_controls/flat_dark/unchecked.png')
        self.me = SpaceCraft(self.w, self.h)
        self.enemy_list = []
        self.start_time = time.time()
        self.enemy_explosion = []
        self.star = [Star(5, 0), Star(25, 0), Star(45, 0)]
        self.score = 0
        self.ex_score = 0
        self.warning_flag = 0
        self.shooting_sound = ':resources:sounds/laser1.mp3'
        self.explosion_sound = ':resources:sounds/explosion2.wav'
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        arcade.draw_text('Score: ', 450, 15, arcade.color.SKY_BLUE,font_size=16)
        arcade.draw_text(str(self.score), 525, 15, arcade.color.SKY_BLUE,font_size=16)
        for i in range(len(self.star)):
            self.star[i].draw()
        self.me.draw()
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()
        for i in range(len(self.enemy_explosion)):
            self.enemy_explosion[i].draw()
        if len(self.star) == 0:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.gameover_background_image)
            arcade.draw_text('GAME OVER', 230, 250, arcade.color.WHITE, font_size=18, bold=True)
            arcade.finish_render()
            time.sleep(3)
            arcade.exit()
            
    def on_update(self, delta_time):
        self.end_time = time.time()
        self.me.rotate()
        round_time = random.randint(3, 7)
        if self.end_time - self.start_time >= round_time:
            self.enemy_list.append(Enemy(self.w, self.h, (2 + (self.score // 10))))
            self.start_time = time.time()
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()
        for i in range(len(self.me.bullet_list)):
            for j in range(len(self.enemy_list)):
                try:
                    if arcade.check_for_collision(self.me.bullet_list[i], self.enemy_list[j]):
                        arcade.Sound(self.explosion_sound).play()
                        self.score += 1
                        try:
                            self.enemy_explosion.append(Explosion(self.enemy_list[j].center_x, self.enemy_list[j].center_y, time.time()))                    
                        except:
                            pass
                        self.me.bullet_list.pop(i)
                        self.enemy_list.pop(j)
                except:
                    pass 
        for i in range(len(self.enemy_explosion)):         
            try:
                if time.time() - self.enemy_explosion[i].time >= 1:
                    self.enemy_explosion.pop(i)
            except:
                pass
        for i in range(len(self.me.bullet_list)):
            try:
                if self.me.bullet_list[i].center_x < 0 or self.me.bullet_list[i].center_y < 0:
                    self.me.bullet_list.pop(i)
            except:
                pass
        for i in range(len(self.enemy_list)):
            try:
                if self.enemy_list[i].center_y < 0:
                    self.star.pop()
                    self.enemy_list.pop(i)
            except:
                pass
                
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_angle = -1
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
        elif key == arcade.key.SPACE:
            self.me.fire(self.shooting_sound)  
            
    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0
    
game = Game()    
arcade.run() 