from enum import Enum
from random import randint

class GridValue(Enum):
    EMPTY = 0
    HEAD  = 1
    BODY  = 2
    FOOD  = 3

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)

class Direction(Pair):
    def __init__(self, x, y):
        super().__init__(x, y)

LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)
UP = Direction(0, -1)
DOWN = Direction(0, 1)

class Position(Pair):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def next_position(self, dir: Direction):
        return Position(self.x + dir.x, self.y + dir.y)


class Game:
    def __init__(self, width, height):
        self.grid = [[GridValue.EMPTY for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.empty = []
        self.food = None
        self.snake = []
        self.game_over = True
    
    def start_game(self):
        for i in range(3):
            self.snake.append(Position(2-i, 0))
        self.direction = RIGHT
        self.update_empty()
        # self.update_food()
        self.food = Position(14, 0)
        self.game_over = False
    
    def change_direction(self, direction):
        if self.direction + direction == Direction(0, 0):
            return
        self.direction = direction

    def update(self):    
        head = self.snake[0]
        next_pos = head.next_position(self.direction)
        print(next_pos.x, next_pos.y)
        if next_pos.x >= self.width or next_pos.x < 0 or next_pos.y >= self.height or next_pos.y < 0:
            self.game_over = True
            return
        if next_pos in self.snake[:-1]:

            self.game_over = True
            return
        self.snake.insert(0, next_pos)
        if next_pos != self.food:
            self.snake.remove(self.snake[-1])
            self.update_empty()
            return True
        else:
            self.update_empty()
            self.update_food()
        
    def update_empty(self):
        self.empty.clear()
        for y in range(self.height):
            for x in range(self.width):
                pos = Position(x, y)
                if pos not in self.snake:
                    self.empty.append(pos)
    
    def update_food(self):
        rand_i = randint(0, len(self.empty)-1)
        self.food = self.empty[rand_i]
        self.empty.remove(self.food)
    
    # def _get_empty(self):
    #     for y in self.grid:
    #         for x in 
        