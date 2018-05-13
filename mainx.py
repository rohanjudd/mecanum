import xbox
from bot import Bot

bot = Bot()
joy = xbox.Joystick()

while not joy.Back():
    # Show connection status
    if joy.connected():
        print("Connected   ",end=" ")
    else:
        print("Disconnected   ", end=" ")
    print("Lx: {:6.3f} Rx: {:6.3f} Ly: {:6.3f} Ry: {:6.3f} ".format(joy.leftX(), joy.rightX(), joy.leftY(), joy.rightY()), end=" ")
    print(chr(13), end = " ")
    bot.analog_control(joy.leftX(),joy.rightX(),joy.leftY(),joy.rightY())
joy.close()
bot.stop()