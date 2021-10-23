import random
import arcade

HEIGHT = 600
WIDTH = 600

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.apple = arcade.Sprite('img/apple.png', scale=0.02)
        self.apple.center_x = random.randint(10, w - 10)
        self.apple.center_y = random.randint(10, h - 10)
        
    def draw(self):
        self.apple.draw()
        
class Pooneh(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.pooneh = arcade.Sprite('img/poop.png', scale=0.05)
        self.pooneh.center_x = random.randint(10, w - 10)
        self.pooneh.center_y = random.randint(10, h - 10)
        
    def draw(self):
        self.pooneh.draw()
    
class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.pear = arcade.Sprite('img/pear.png', scale=0.11)
        self.pear.center_x = random.randint(10, w - 10)
        self.pear.center_y = random.randint(10, h - 10)
        
    def draw(self):
        self.pear.draw()

class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.GREEN
        self.bodycolor = arcade.color.GREEN_YELLOW
        self.speed = 1
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 1
        self.body = []
        self.body.append([self.center_x, self.center_y])
        
    def draw(self):
        for i in range(len(self.body)):
            if i == 0:
                arcade.draw_circle_filled(self.body[i][0], self.body[i][1], self.r, self.color)
            else:
                arcade.draw_circle_outline(self.body[i][0], self.body[i][1], self.r, self.bodycolor)

    def move(self, appleX, appleY):
        self.change_x = 0
        self.change_y = 0
        
        if self.center_x > appleX:
            self.change_x = -1
        if self.center_x < appleX:
            self.change_x = 1        
        if self.center_x == appleX:
            self.change_x = 0
            if self.center_y > appleY:
                self.change_y = -1
            if self.center_y < appleY:
                self.change_y = 1
            if self.center_y == appleY:
                self.change_y = 0
        
        for i in range(len(self.body)-1, 0, -1):
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
                
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y

    def eat(self, mode):
        if mode == 0: # for eat apple
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
        
        elif mode == 1: # for eat pooneh
            self.score -= 1
            self.body.pop()
            
        elif mode == 2: # for eat pear
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
    
class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, WIDTH, HEIGHT, "Super Snake")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(WIDTH, HEIGHT)
        self.apple = Apple(WIDTH, HEIGHT)
        self.pooneh = Pooneh(WIDTH, HEIGHT)
        self.pear = Pear(WIDTH, HEIGHT)
        
    def on_draw(self):
        # نمایش دادن اشیا موجود در بازی
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pooneh.draw()
        self.pear.draw()
        arcade.draw_text('SCORE : ', 20, HEIGHT - 25, arcade.color.BLACK)
        arcade.draw_text(str(self.snake.score), 100, HEIGHT - 25, arcade.color.BLACK, italic=True)
        if self.snake.score == 0 or self.snake.center_x < 0 or self.snake.center_x > WIDTH or self.snake.center_y < 0 or self.snake.center_y > HEIGHT:
            arcade.draw_text('GAME OVER !', WIDTH // 2, HEIGHT // 2, bold=True, font_size=18)
            arcade.exit()
            
    def on_update(self, delta_time: float):
        # تمام منطق و اتفاقات بازی در این تابع رخ میدهد
        self.snake.move(self.pear.pear.center_x, self.pear.pear.center_y)
        if arcade.check_for_collision(self.apple.apple, self.snake): # (self.apple.center_x == self.snake.center_x) and (self.apple.center_y == self.snake.center_y)
            self.snake.eat(0)
            self.apple = Apple(WIDTH, HEIGHT)
            
        if arcade.check_for_collision(self.pooneh.pooneh, self.snake): 
            self.snake.eat(1)
            self.pooneh = Pooneh(WIDTH, HEIGHT)
            
        if arcade.check_for_collision(self.pear.pear, self.snake): 
            self.snake.eat(2)
            self.pear = Pear(WIDTH, HEIGHT) 
        
if __name__ == '__main__':
    game = Game()
    arcade.run()