import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT
from wheel import Wheel

FL_id = 2
FR_id = 1
RL_id = 3
RR_id = 4

trim = [0, 0, 0, 0]

i2c_address = 0x60


class Bot:
    def __init__(self):
        self.motor_controller = Adafruit_MotorHAT(i2c_address)
        self.FL = Wheel(self.motor_controller, FL_id, trim[0], invert=True)
        self.FR = Wheel(self.motor_controller, FR_id, trim[1], invert=True)
        self.RL = Wheel(self.motor_controller, RL_id, trim[2])
        self.RR = Wheel(self.motor_controller, RR_id, trim[3])

        self.all_wheels = [self.FL, self.FR, self.RL, self.RR]
        self.left_wheels = [self.FL, self.RL]
        self.right_wheels = [self.FR, self.RR]
        self.left_diag = [self.FL, self.RR]
        self.right_diag = [self.FR, self.RL]
        atexit.register(self.stop)
        self.stop()

    def analog_control(self, x0, x1, y0, y1):
        for w in self.left_wheels:
            w.set_speed(y0)
        for w in self.right_wheels:
            w.set_speed(y1)
        for w in self.left_diag:
            w.add_mix(x0)
        for w in self.right_diag:
            w.add_mix(x1)
        for w in self.all_wheels:
            w.update_speed()

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

    def inv_test(self):
        self.FL.switch_invert()





