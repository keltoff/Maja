import pos_math as pmath
from ent import Entity


class Creep(Entity):
    def __init__(self, x=0, y=0):
        Entity.__init__(self, x, y)

    def update(self, dt):
        Entity.update(self, dt)

    def move(self, dist):
        target = self.eng.mc.pos

        self.tail = self.pos
        self.tail_duration = 500

        self.pos = pmath.close(self.pos, target, 0.2 * dist, 100)