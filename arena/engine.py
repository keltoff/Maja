
class Engine(object):
    def __init__(self):
        self.mc = None
        self.creeps = []
        self.spawners = []

    def all_components(self):
        yield self.mc

        for c in self.creeps:
            yield c

        for s in self.spawners:
            yield s

    def turn(self):
        for com in self.all_components():
            com.upd_turn()

    def tick(self, t):
        for com in self.all_components():
            com.upt_time(t)

    def update(self, t):
        for com in self.all_components():
            com.update(t)

    def add(self, creep):
        self.creeps.append(creep)
        creep.eng = self

    def add_spawn(self, spawn):
        self.spawners.append(spawn)
        spawn.eng = self

    @classmethod
    def build(cls):
        return Engine()