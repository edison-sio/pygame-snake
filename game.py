from enum import Enum

class GridValue(Enum):
    EMPTY = 0
    HEAD  = 1
    BODY  = 2
    FOOD  = 3

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Direction:
    def __init__(self, x, y):
        Pair(x, y)

class Position:
    def __init__(self, x, y):
        Pair(x, y)
    
    def next_position(self, dir: Direction):
        return Position(self.x + dir.x, self.y + dir.y)


class Game:
    def __init__(self, width, height):
        self.grid = [[GridValue.EMPTY for _ in range(width)] for _ in range(height)]
        self.food = None
        self.snake = []
    
    def start_game(self):
        for i in range(3):
            self.snake.append(Position(i, 0))
        