import curses
import time
#Зробити другу зірку 
class Anime:
    def __init__(self, window):
        self.window = window
        self.x_right = 0
        self.x_left = self.window.getmaxyx()[1] - 1
        self.y = 0
        
        
    def animate(self):
        while True:
            self.window.clear()
            """for i in range(2):
                self.window.addch(self.y, (self.x + i) % self.window.getmaxyx()[1], '*')"""
            self.window.addch(self.y, self.x_left, '*')
            self.window.addch(self.y, self.x_right, '*')
            self.window.refresh()
            time.sleep(0.1)
            self.x_left = (self.x_left - 1) % self.window.getmaxyx()[1]
            self.x_right = (self.x_right + 1) % self.window.getmaxyx()[0]
            self.y = (self.y + 1) % self.window.getmaxyx()[0]


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    animation = Anime(stdscr)
    animation.animate()
curses.wrapper(main)
