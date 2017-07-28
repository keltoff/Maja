import pos_math as pmath


class Entity(object):
    def __init__(self, x=0, y=0):
        self.pos = (x, y)
        self.eng = None

        self.tail = None
        self.tail_duration = None

    def update(self, dt):
        if self.tail:
            self.tail_duration -= dt
            if self.tail_duration < 0:
                self.tail = None

    def move(self):
        pass

    @property
    def ipos(self):
        return pmath.ipos(self.pos)