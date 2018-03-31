import atexit

from Adafruit_MotorHAT import Adafruit_MotorHAT
from wheel import Wheel

FL_id = 1
FR_id = 2
RL_id = 3
RR_id = 4

trim = [0, 0, 0, 0]

i2c_address = 0x60


class Bot:
    def __init__(self):
        self.motor_controller = Adafruit_MotorHAT(i2c_address)
        self.FL = Wheel(self.motor_controller, FL_id, trim[0])
        self.FR = Wheel(self.motor_controller, FR_id, trim[1], invert=True)
        self.RL = Wheel(self.motor_controller, RL_id, trim[2])
        self.RR = Wheel(self.motor_controller, RR_id, trim[3], invert=True)

        self.all_wheels = [self.FL, self.FR, self.RL, self.RR]
        self.left_wheels = [self.FL, self.RL]
        self.right_wheels = [self.FR, self.RR]
        self.left_diag = [self.FL, self.RR]
        self.right_diag = [self.FR, self.RL]
        atexit.register(self.stop)
        self.stop()

    def stop(self):
        for w in self.all_wheels:
            w.stop()

    def forward(self, speed):
        for w in self.all_wheels:
            w.write_speed(speed)

    def backward(self, speed):
        for w in self.all_wheels:
            w.write_speed(speed*-1)

    def left(self, speed):
        for w in self.left_wheels:
            w.write_speed(speed*-1)
        for w in self.right_wheels:
            w.write_speed(speed)

    def right(self, speed):
        for w in self.left_wheels:
            w.write_speed(speed)
        for w in self.right_wheels:
            w.write_speed(speed*-1)

    def strafe_left(self, speed):
        for w in self.left_diag:
            w.write_speed(speed*-1)
        for w in self.right_diag:
            w.write_speed(speed)

    def strafe_right(self, speed):
        for w in self.left_diag:
            w.write_speed(speed)
        for w in self.right_diag:
            w.write_speed(speed*-1)





