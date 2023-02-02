import pygame as pg
import os

from game import Game

# WIN = pg.display.set_mode((500, 500))
clock = pg.time.Clock()

class SnakeGameWindow:
    def __init__(self, title: str='Snake Game', 
                 width: int=900, 
                 height: int=500, 
                 fps: int=60,
                 theme: str='') -> None:
        '''
        Initiate snake game window
        '''
        # Windows init
        self.win = pg.display.set_mode((width, height))
        self.fps = fps
        self.game = Game()
        
        # Game init
        # self.background = pg.image.load(os.path.join('Assets', {theme}, 'background.png'))
        self.background = (255, 255, 255)
        self.head = pg.transform.scale(pg.image.load(os.path.join('Assets', 'head.png')), (100, 100))
        # self.body = pg.image.load(os.path.join('Assets', {theme}, 'body.png'))
        # self.food = pg.image.load(os.path.join('Assets', {theme}, 'food.png'))
        # self.empty = pg.image.load(os.path.join('Assets', {theme}, 'empty.png'))
        


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
        self._draw_window()
        clock.tick(self.fps)
    
    def _draw_window(self):
        self.win.fill(self.background)
        # self.win.blit(self.head, (0, 0))
        for y in range(5):
            for x in range(9):
                # print(row, col)
                self.win.blit(self.head, (x*100, y*100))
        pg.display.update()

if __name__ == '__main__':
    app = SnakeGameWindow()
    app.mainloop()