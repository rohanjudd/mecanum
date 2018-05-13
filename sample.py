import xbox


# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)


joy = xbox.Joystick()

print
"Xbox controller sample: Press Back button to exit"
# Loop until back button is pressed
while not joy.Back():
    # Show connection status
    if joy.connected():
        print("Connected   ",end=" ")
    else:
        print("Disconnected   ", end=" ")
    # Left analog stick
    print("Lx: {:6.3f},Ly: {:6.3f} ".format(joy.leftX(), joy.rightX(), joy.leftY(), joy.rightY()))
    print(chr(13), end = " ")
    bot.analog_control(joy.leftX(),joy.rightX(),joy.leftY(),joy.rightY())
# Close out when done
joy.close()