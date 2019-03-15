
class Engine(object):
    def __init__(self):
        self.mc = None
        self.creeps = []
        self.spawners = []
        self.ground_effs = []
        self.sky_effs = []

    def all_components(self):
        yield self.mc

        for c in self.creeps:
            yield c

        for s in self.spawners:
            yield s

        for e in self.ground_effs:
            yield e

        for e in self.sky_effs:
            yield e

    def turn(self):
        for com in self.all_components():
            com.upd_turn()

    def tick(self, t):
        for com in self.all_components():
            com.upt_time(t)

    def update(self, t):
        for com in self.all_components():
            com.update(t)

        self.purge()

    def purge(self):
        def purge_dead(values):
            return list(filter(lambda v: v.alive(), values))

        self.creeps = purge_dead(self.creeps)
        self.ground_effs = purge_dead(self.ground_effs)
        self.sky_effs = purge_dead(self.sky_effs)

    def add(self, creep):
        self.creeps.append(creep)
        creep.eng = self

    def add_spawn(self, spawn):
        self.spawners.append(spawn)
        spawn.eng = self

    def add_eff(self, eff, ground=False):
        if ground:
            self.ground_effs.apend(eff)
        else:
            self.sky_effs.append(eff)
        eff.eng = self

    @classmethod
    def build(cls):
        return Engine()