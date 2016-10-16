
import pygame, sys
from pygame import constants as c
from twenty48 import Board_2048
import copy

# Shell script for converting images:
# for filename in *.ico; do name=$(basename $filename .ico);
# convert $name.ico -type truecolormatte PNG32:$name.png;
# mv $name-0.png $name.png; rm *-[12345].png; done

class Tile(object):
    def __init__(self, image, x1, y1, x2, y2, step=5):
        self.image = image
        # if x1 > x2:
        #     xstep = -1
        # ...
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.step = step

    def move(self):
        # x += self.xstep
        # if x == x2:
        #     self.xstep = 0
        if self.x < self.x2:
            self.x += self.step
        elif self.x > self.x2:
            self.x -= self.step
        if self.y < self.y2:
            self.y += self.step
        elif self.y > self.y2:
            self.y -= self.step

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def done(self):
        return self.x == self.x2 and self.y == self.y2

def main():
    board = Board_2048()
    screen = pygame.display.set_mode((320, 320))
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    clock = pygame.time.Clock()
    score = -1
    add_score = +1
    tiles = list()
    tile_images = {}
    tile = None   # todo: change to a list of tiles
    moves = list()
    for number in ('0', '2', '4', '8', '16', '32', '64', '128', '256', '512'):
        filename = 'static/{}.jpg'.format(number)
        image = pygame.image.load(filename)
        image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (76, 76))
        tile_images[number] = image

    while True:
        old_board = copy.deepcopy(board)

        for event in pygame.event.get():
            if event.type == c.KEYDOWN:
                if event.key == c.K_ESCAPE:
                    sys.exit(0)

                # NEW:
                elif event.key == c.K_RIGHT:
                    board, moves, add_score = board.right()
                    print moves
                elif event.key == c.K_LEFT:
                    board, moves, add_score = board.left()
                    print moves
                elif event.key == c.K_UP:
                    board, moves, add_score = board.up()
                    print moves
                elif event.key == c.K_DOWN:
                    board, moves, add_score = board.down()
                    print moves
        while moves:    
            i1, j1, i2, j2 = moves.pop()  # todo: make a tile for every item
            number = old_board.rows[i1][j1]
            image = tile_images[str(number)]
            tiles.append(Tile(image, j1 * 80, i1 * 80, j2 * 80, i2 * 80))
                
        if add_score:
            score += add_score
            add_score = 0
            label = 'Score: %s' % score
            label_1 = myfont.render(label, 1, (0,0,0))

        screen.fill((255, 255, 255))
        for a in range(0,3):
            for b in range(0,3):
                e = 80 * a
                f = 80 * b
                pygame.draw.rect(screen, (0,0,0), (e,f,80,80), 1)
        
        for i in range(0,3):
            j = 0
            for number in board.rows[i]:
                x = 80 * j + 2
                y = 80 * i + 2
                j += 1
                number = '%s' % number
                screen.blit(tile_images[number], (x, y))            
        for tile in tiles:
            if tile is not None:
                tile.blit(screen)
                tile.move()
                if tile.done():
                    tiles.remove(tile)
        
        screen.blit(label_1, (2,250))

        pygame.display.flip()
        clock.tick(60)
        moves = set()
if __name__ == "__main__":
    main()
    
