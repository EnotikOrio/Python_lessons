import curses
import time
import random
#Сделать что бы звезда ходила вверх и вниз а потом сделать что бы это работало с 3-4 звёздами
class Star:
    def __init__(self, window, y, x):
        self.window = window
        self.y = y
        self.x = x
        self.y_direction = 1 if random.choice([True, False]) else -1
        self.x_direction = 1 if random.choice([True, False]) else -1

    def move(self):
        self.y += self.y_direction
        self.x += self.x_direction

        if self.y <= 0 or self.y >= self.window.getmaxyx()[0] - 1:
            self.y_direction *= -1
        if self.x <= 0 or self.x >= self.window.getmaxyx()[1] - 1:
            self.x_direction *= -1

    def draw(self):
        self.window.addch(self.y, self.x, '*')

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    stars = []
    for _ in range(3):
        y = random.randint(0, stdscr.getmaxyx()[0] - 1)
        x = random.randint(0, stdscr.getmaxyx()[1] - 1)
        stars.append(Star(stdscr, y, x))

    while True:
        stdscr.clear()

        for star in stars:
            star.move()
            star.draw()

        stdscr.refresh()
        time.sleep(0.1)

curses.wrapper(main)
