
class Engine(object):
    def __init__(self):
        self.mc = None
        self.creeps = []

    def turn(self):
        turn_len = 200
        self.mc.move(turn_len)

        for c in self.creeps:
            c.move(turn_len)

    def tick(self, t):
        self.mc.move(t)

        for c in self.creeps:
            c.move(t)

    def update(self, t):
        self.mc.update(t)

        for c in self.creeps:
            c.update(t)

    def add(self, creep):
        self.creeps.append(creep)
        creep.eng = self

    @classmethod
    def build(cls):
        return Engine()