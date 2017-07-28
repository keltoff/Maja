import pos_math as pmath
from ent import Entity


class Main(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)

        self.target = None
        self.speed = 0.5

    def update(self, t):
        Entity.update(self, t)

    def move(self, dist):
        if self.target:

            self.tail = self.pos
            self.tail_duration = 500

            self.pos = pmath.close(self.pos, self.target, dist*self.speed, 0)
            if pmath.distance(self.pos, self.target) < self.speed:
                self.target = None