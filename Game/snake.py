import pygame


class Snake:
    def __init__(self):

        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):
        """"Direction of snake"""
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        """Add new head to the list body and delete tail"""
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """Draw snake on monitor"""
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("Blue"), pygame.Rect(segment[0], segment[1], 10, 10))

    def check_end_window(self):
        """Check reaching the end of field"""
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, gui):
        """Eating food"""
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def cheak_barrier(self, gui):
        """Check snake's bumpt into"""
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicator.pop()
            gui.game = "LOSE"
        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicator.pop()
            gui.game = "LOSE"
