from Adafruit_MotorHAT import Adafruit_MotorHAT
IN_CENTRE = 0
IN_MIN = -1
IN_MAX = 1

OUT_CENTRE = 0
OUT_MIN = -255
OUT_MAX = 255


def map_speed(x):
    return (x - IN_MIN) * (OUT_MAX - OUT_MIN) / (IN_MAX - IN_MIN) + OUT_MIN


def constrain(x):
    return min(IN_MAX, max(IN_MIN, x))


class Wheel:
    def __init__(self, controller, motor_id, trim, invert=False):
        self.id = motor_id
        self.invert = invert
        self.trim = trim
        self.motor = controller.getMotor(self.id)
        self.speed = 0
        self.release()

    def switch_invert(self):
        self.invert = not self.invert

    def release(self):
        self.motor.run(Adafruit_MotorHAT.RELEASE)

    def forward(self):
        self.motor.run(Adafruit_MotorHAT.FORWARD)

    def backward(self):
        self.motor.run(Adafruit_MotorHAT.BACKWARD)

    def stop(self):
        self.speed = 0
        self.release()

    def reset_speed(self):
        speed = 0

    def add_mix(self, amount):
        self.speed += amount
        self.speed = constrain(self.speed)

    def set_speed(self, speed):
        self.speed = constrain(speed)

    def write_speed(self, speed):
        self.speed = constrain(speed)
        #print("id: {}  speed: {}  self.speed: {}".format(self.id, speed, self.speed))
        self.update_speed()

    def update_speed(self):
        out_speed = map_speed(self.speed)
        out_speed += self.trim
        if self.invert:
            #print("inverting")
            out_speed = out_speed*-1
        #print("id: {}  inv: {}  in_speed: {} out_speed: {}".format(self.id, self.invert, self.speed, out_speed))
        self.motor.setSpeed(int(abs(out_speed)))
        if out_speed >= 0:
            self.forward()
            #print("id: {}  forward".format(self.id))
        else:
            self.backward()
            #print("id: {}  backward".format(self.id))
        #self.forward() if out_speed >= 0 else self.backward()







