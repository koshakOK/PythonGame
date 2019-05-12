import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")
control1 = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)
var_speed = 0
while control1.flag_game:
    gui.win_lose()
    control1.control()
    window.fill(pygame.Color("White"))
    gui.draw_monitor(window)
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
        gui.draw_level(window)
        gui.draw_indicator(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)
    if var_speed % 2 == 0 and control1.flag_pause and gui.game == "GAME":
        snake.cheak_barrier(gui)
        snake.move(control1)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 1
    pygame.display.flip()
