import curses
import time
import random

cord_x = []
cord_y = []

#Зробити другу зірку 
class Anime:
    def __init__(self, window):
        self.window = window
        self.x = 0
        self.y = 0
        
        
    def animate(self):
        for i in range(1, 500):
            #self.window.clear()
            """for i in range(2):
                self.window.addch(self.y, (self.x + i) % self.window.getmaxyx()[1], '*')"""
            r1 = random.randint(0, 5)
            self.window.addch(self.y, self.x, '*')
            cord_x.append(self.x)
            cord_y.append(self.y)
            for j in range(0, r1):
                self.window.addch(self.y, self.x, ' ')
            self.window.refresh()
            time.sleep(0.001)
            self.x = (self.x + 1) % self.window.getmaxyx()[1]
            if i % 150 == 0:
                self.x = 0
                self.y = (self.y + 1) % self.window.getmaxyx()[0]

            


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    animation = Anime(stdscr)
    animation.animate()
curses.wrapper(main)
print(cord_x)
print()
print(cord_y)
