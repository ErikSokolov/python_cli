import sys
import os
import time
import curses

def main(stdscr):
    curses.curs_set(0)
    def screen():
        s = 1
        try:
            while True:
                stdscr.clear()
                stdsr.addstr(0, 0, 'foo')
                key = std.getch()
                if key == curses.KEY_DOWN:
                    print('foo')
                def game():
                    s = 1
                    x = 0
                    v = "@"
                    maxx = 100


                    while True: 
                        time.sleep(s)

                        


                        






                        print(" "*x + v) 
                        x += 1
                        
                        if v == "@":
                            v = "#"
                        elif v == "#":
                            v = "@"

                        






                
                game()
                time.sleep(s)
                os.system('cls' if os.name == 'nt' else 'clear')
        except KeyboardInterrupt:
            sys.exit()
    
    screen()
if __name__ == "__main__":
    main()
