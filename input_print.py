import curses
import time
#import os

def main(window):
    x = 0
    curses.curs_set(0)
    window.nodelay(True)
    window.clear()

    while True:
        key = window.getch()

        window.clear()

        window.addstr(0,0, f"foo {x}")

        if key == ord('q'):
            x += 1 

        window.refresh()

        time.sleep(0.2)

    

curses.wrapper(main)


