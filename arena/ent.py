import pos_math as pmath
import pygame


class Entity(object):
    def __init__(self, x=0, y=0):
        self.pos = (x, y)
        self.eng = None

        self.tail = None
        self.tail_duration = None

        self.turn_length = 200
        self.turn_elapsed = 0

    def update(self, dt):
        if self.tail:
            self.tail_duration -= dt
            if self.tail_duration < 0:
                self.tail = None

    def ticks(self, dt):
        pass

    def turn(self):
        pass

    def move(self):
        pass

    def upd_time(self, dt):
        self.ticks(dt)

        self.turn_elapsed += dt
        if self.turn_elapsed >= self.turn_length:
            self.turn_elapsed -= self.turn_length
            self.turn()

    def upd_turn(self):
        self.ticks(self.turn_length)
        self.turn()

    @property
    def ipos(self):
        return pmath.ipos(self.pos)

    def draw(self, screen):
        pass