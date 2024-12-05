import curses
import os
import time

def main(window):
    x = 0
    while True:
        time.sleep(1)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'foo{x}', end = "\n This is a test") 



        #window.addstr(f"bar{x}")
        x += 1
        #window.refresh()
        #window.getch()

    

curses.wrapper(main)


