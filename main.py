import time
import curses

from bot import Bot


def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True:
            ch = win.getch()
            if ch in range(32, 127):
                break
            time.sleep(0.05)
    except:
        raise
    finally:
        curses.endwin()
    return chr(ch)

bot = Bot()

speed = 1


def close():
    bot.stop()
    quit()

while True:
    inp = input_char("wasd controls: ")
    if inp == 'w':
        bot.forward(1)
    elif inp == 's':
        bot.backward(1)
    elif inp == 'q':
        bot.left(1)
    elif inp == 'e':
        bot.right(1)
    elif inp == 'a':
        bot.strafe_left(1)
    elif inp == 'd':
        bot.strafe_right(1)
    elif inp == 'x':
        bot.stop()
    elif inp == 'q':
        close()
    time.sleep(0.5)




