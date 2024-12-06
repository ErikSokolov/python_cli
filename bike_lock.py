import curses
import time
import random

def main(window):
    curses.curs_set(1)
    window.nodelay(True)

    ran_x = random.randint(0,2)
    ran_y = random.randint(0,2)


    x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    i = 0

    y = [[9], [8], [7], [6], [5], [4], [3], [2], [1], [0]]
    a = 0


    while True:
        key = window.getch()

        window.clear()

      
        window.addstr(0,0, f"{x[i-1][0]} | {y [a-1][0]}")
        window.addstr(1,0, f"{x[i][0]} | {y[a][0]}")
        window.addstr(2,0, f"{x[i+1][0]} | {y[a+1][0]}")


        if key == ord('h'):
            if i < x[-1][-1]:
                i += 1
            else:
                window.addstr(0,0, f"toooomuchhhh")

        if key == ord('l'):
            if i > x[0][0]:
                i -= 1
            else:
                window.addstr(0,0,f"toooooolittttle")
        


        if key == ord('j'):
            if a < y[0][0]:
                a += 1
            else:
                window.addstr(0,0, f"toooolittle")

        if key == ord('k'):
            if a > y[-1][-1]:
                a -= 1
            else:
                window.addstr(0,0,f"tomuch")

            


        time.sleep(0.1)


        if i == ran_x and a == ran_y:
            return False

    else:
        window.addstr(0,0,f"open")

    

           



curses.wrapper(main)


