import time
import arcade
from player import Player
from ground import Ground, Box
from enemy import Enemy
from star import Star

class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 700
        self.gravity = 0.2
        super().__init__(self.w, self.h, 'Platformer Game - ALI')
        self.background_image = arcade.load_texture('images\jungle_background.png')
        self.t1 = time.time()
        self.key_time = time.time()
        self.key = arcade.Sprite(':resources:images/items/keyYellow.png')
        self.key.center_x = 160
        self.key.center_y = 480
        self.key.width = 50
        self.key.height = 50
        self.lock = arcade.Sprite(':resources:images/tiles/lockYellow.png')
        self.lock.center_x = 930
        self.lock.center_y = 130
        self.lock.width = 50
        self.lock.height = 50
        self.door = arcade.Sprite(':resources:images/tiles/doorClosed_mid.png')
        self.door.center_x = 730
        self.door.center_y = 590
        self.door.width = 60
        self.door.height = 60
        self.me = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        for i in range(0, 1200, 130):
            ground = Ground(i, 40)
            self.ground_list.append(ground)
        for i in range(500, 700, 120):
            box = Box(i, 240)
            self.ground_list.append(box)
        for i in range(180, 280, 120):
            box = Box(i, 400)
            self.ground_list.append(box)
        for i in range(700, 750, 120):
            box = Box(i, 500)
            self.ground_list.append(box)
        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, gravity_constant=self.gravity)
        self.enemy_physics_engine_list = []
        self.star = [Star(35, 670), Star(65, 670), Star(95, 670)]
        self.zombie_sound = ':resources:sounds/hurt1.wav'
        self.finish_background_image = arcade.load_texture(':resources:onscreen_controls/flat_dark/unchecked.png')
        self.eat_time = 0
        self.door_flag = 0

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
        if time.time() - self.key_time > 5:
            try:
                self.key.draw()
            except:
                pass
        self.lock.draw()
        if self.door_flag == 1:
            self.door.draw()
        self.me.draw()
        for ground in self.ground_list:
            ground.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for i in range(len(self.star)):
            self.star[i].draw()
        if len(self.star) == 0:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.finish_background_image)
            arcade.draw_text('GAME OVER', 410, 350, arcade.color.RED, font_size=20, bold=True)
            arcade.finish_render()
            time.sleep(3)
            arcade.exit()
        if self.door_flag == 1 and arcade.check_for_collision(self.me, self.door):
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.finish_background_image)
            arcade.draw_text('YOU WIN', 410, 350, arcade.color.WHITE, font_size=20, bold=True)
            arcade.finish_render()
            time.sleep(3)
            arcade.exit()
        
    def on_update(self, delta_time: float):
        self.t2 = time.time()
        if self.t2 - self.t1 > 5:
            new_enemy = Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy, self.ground_list, gravity_constant=self.gravity))
            self.t1 = time.time()
        self.my_physics_engine.update()
        for i in range(len(self.enemy_physics_engine_list)):
            self.enemy_physics_engine_list[i].update()
        for enemy in self.enemy_list:
            enemy.update_animation()
        self.me.update_animation()
        try:
            if arcade.check_for_collision(self.me, self.key):
                self.me.pocket.append(self.key)
                del self.key
        except:
            pass
        if len(self.me.pocket) == 1 and arcade.check_for_collision(self.me, self.lock):
            self.lock.texture = arcade.load_texture(':resources:images/items/flagGreen2.png')
            self.door_flag = 1
        for enemy in self.enemy_list:
            try:
                if enemy.center_x < -5 or enemy.center_x < 1005:
                    del enemy
            except:
                pass
        for enemy in self.enemy_list:
            if time.time() - self.eat_time > 3:
                try:
                    if arcade.check_for_collision(self.me, enemy):
                        arcade.Sound(self.zombie_sound).play()
                        self.star.pop()
                        self.eat_time = time.time()
                except:
                    pass 
                
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = -1 * self.me.speed
        elif key == arcade.key.RIGHT:
            self.me.change_x = 1 * self.me.speed
        elif key == arcade.key.UP and self.my_physics_engine.can_jump():
            self.me.change_y = 10           
            
    def on_key_release(self, key, modifiers):
        self.me.change_x = 0
            
game = Game()
arcade.run()