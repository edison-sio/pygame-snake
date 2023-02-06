import pygame as pg
import os

from game import Game, LEFT, RIGHT, UP, DOWN

# WIN = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

class SnakeGameWindow:
    def __init__(self, title: str='Snake Game', 
                 width: int=500, 
                 height: int=500, 
                 fps: int=60,
                 theme: str='default') -> None:
        '''
        Initiate snake game window
        '''
        # Windows init
        self.win = pg.display.set_mode((width, height))
        self.fps = fps
        self.game = Game(23, 23)
        self.game.start_game()

        self.frame_count = 0

        self.block_side = 20
        
        # Game init
        # self.background = pg.image.load(os.path.join('Assets', {theme}, 'background.png'))
        self.background = (25, 25, 25)
        self.head = pg.transform.scale(pg.image.load(os.path.join('assets', theme, 'body.png')), (self.block_side, self.block_side))
        self.body = pg.transform.scale(pg.image.load(os.path.join('Assets', theme, 'body.png')), (self.block_side, self.block_side))
        self.food = pg.transform.scale(pg.image.load(os.path.join('Assets', theme, 'food.png')), (self.block_side, self.block_side))
        self.empty = pg.transform.scale(pg.image.load(os.path.join('Assets', theme, 'empty.png')), (self.block_side, self.block_side))
        
        pg.display.set_caption(title)

    def mainloop(self):
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self._update()
        pg.quit()
    
    def _update(self):
        clock.tick(self.fps)
        
        keys_pressed = pg.key.get_pressed()
        if keys_pressed[pg.K_LEFT]:
            self.game.change_direction(LEFT)
        if keys_pressed[pg.K_RIGHT]:
            self.game.change_direction(RIGHT)
        if keys_pressed[pg.K_UP]:
            self.game.change_direction(UP)
        if keys_pressed[pg.K_DOWN]:
            self.game.change_direction(DOWN)
        
        if self.frame_count == self.block_side: 
            if self.game.update():
                self.fps += 1
            self.frame_count = 0
        self.frame_count += 1
        self._draw_window()
    
    def _draw_window(self):
        self.win.fill(self.background)
        empty_positions = self.game.empty
        snake_positions = self.game.snake
        food_position = self.game.food

        # Draw empty
        for pos in empty_positions:
            self.win.blit(self.empty, ((pos.x+1) * self.block_side, (pos.y+1) * self.block_side))
        
        # Draw snake
        is_head = True
        for pos in snake_positions:
            if is_head:
                self.win.blit(self.head, ((pos.x+1) * self.block_side, (pos.y+1) * self.block_side))
                is_head = False
            else:
                self.win.blit(self.body, ((pos.x+1) * self.block_side, (pos.y+1) * self.block_side))
        
        # Draw food
        self.win.blit(self.food, ((food_position.x+1) * self.block_side, (food_position.y+1) * self.block_side))
                
        pg.display.update()

if __name__ == '__main__':
    app = SnakeGameWindow()
    app.mainloop()