import pygame.draw as pd
from pygame.color import Color

class Effect:
    def __init__(self):
        self.eng = None

    def update(self, dt):
        pass

    def upd_time(self, dt):
        pass

    def upd_turn(self):
        pass

    def draw(self, screen):
        pass

    def alive(self):
        return True


class Ring(Effect):
    def __init__(self, pos):
        self.pos = pos
        self.duration = 1000
        self.max_r = 100

        self.t = 0

    def update(self, dt):
        self.t += dt

    def draw(self, screen):
        r = int(self.max_r * float(self.t) / self.duration)
        w = min(r, 2)
        pd.circle(screen, Color('black'), self.pos, r, w)

    def alive(self):
        return self.t < self.duration


class Beam(Effect):
    def __init__(self, origin, target, color=Color('cyan'), width=10, duration=1000):
        self.origin = origin
        self.duration = duration
        self.color = color
        self.width = width
        self.edge_pt = target

    def update(self, dt):
        self.duration -= dt

    def alive(self):
        return self.duration >= 0

    def draw(self, screen):
        pd.line(screen, self.color, self.origin, self.edge_pt, self.width)