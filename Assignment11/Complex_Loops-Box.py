import arcade

arcade.open_window(width=700, height=700, window_title='Complex Loops - Box')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

blue = arcade.color.BLUE
red = arcade.color.RED
x = 200
y = 500
w = 15
h = 15
a = 45

for j in range(10):
    for i in range(10):    
        if (i + j) % 2 == 0:
            arcade.draw_rectangle_filled(x, y, w, h, blue, a)
        else:
            arcade.draw_rectangle_filled(x, y, w, h, red, a)
        x += 30
    x = 200
    y -= 30

arcade.finish_render()
arcade.run()
