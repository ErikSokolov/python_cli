import curses

def main(window):
    window.clear()

    window.addstr("foo")

    window.refresh()

    window.getch()

curses.wrapper(main)
