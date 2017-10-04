
class Engine(object):
    def __init__(self):
        self.mc = None
        self.creeps = []
        self.spawners = []

    def turn(self):

        self.mc.upd_turn()

        for c in self.creeps:
            c.upd_turn()

        for s in self.spawners:
            s.upd_turn()

    def tick(self, t):
        self.mc.upd_time(t)

        for c in self.creeps:
            c.upd_time(t)

        for s in self.spawners:
            s.upd_time(t)

    def update(self, t):
        self.mc.update(t)

        for c in self.creeps:
            c.update(t)

        for s in self.spawners:
            s.update(t)

    def add(self, creep):
        self.creeps.append(creep)
        creep.eng = self

    def add_spawn(self, spawn):
        self.spawners.append(spawn)
        spawn.eng = self

    @classmethod
    def build(cls):
        return Engine()