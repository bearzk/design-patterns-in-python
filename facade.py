class Robot(object):
    def __init__(self):
        self.brain = Brain()
    def speak(self):
        self.brain.speak()
    def wave(self):
        self.brain.wave()
    def move(self):
        self.brain.move()


class Mouth(object):
    def speak(self):
        print "spoke a word."

class Arm(object):
    def wave(self):
        print "waved a bit."

class Leg(object):
    def move(self):
        print "twitched a bit."

class Brain(object):
    def __init__(self):
        self.mouth = Mouth()
        self.arm = Arm()
        self.leg = Leg()

    def speak(self):
        self.mouth.speak()

    def wave(self):
        self.arm.wave()

    def move(self):
        self.leg.move()


robot = Robot()
robot.speak()
robot.wave()
robot.move()
