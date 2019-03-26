import computations as cmp
import pygame.draw as pd
from pygame.color import Color
from arena.effect import Beam, Ring
import sys


class Laser:
    def __init__(self, width=10):
        self.targeting_line = None
        self.width = width
        self.length = sys.maxint
        self.name = 'Beam'

    def targeting(self, origin, cursor):
        self.targeting_line = cmp.Line(origin, cursor)

    def draw_cursor(self, canvas, origin, target):
        tx, ty = target
        size = 5
        color = Color('black')
        pd.line(canvas, color, (tx - size, ty), (tx + size, ty))
        pd.line(canvas, color, (tx, ty - size), (tx, ty + size))

    def targets(self, target_candidate):
        od, ld = self.targeting_line.get_distance(target_candidate.pos)
        return 0 <= od <= self.length and ld <= self.width

    def draw_aimmark(self, canvas, origin, target):
        tx, ty = target.pos
        size = 8
        gap = 4
        color = Color('red')
        pd.line(canvas, color, (tx - size, ty - size), (tx - gap, ty - gap))
        pd.line(canvas, color, (tx + size, ty - size), (tx + gap, ty - gap))
        pd.line(canvas, color, (tx + size, ty + size), (tx + gap, ty + gap))
        pd.line(canvas, color, (tx - size, ty + size), (tx - gap, ty + gap))

    def proc(self, engine, target):
        self.targeting(engine.mc.pos, target)

        for will in engine.creeps:
            if self.targets(will):
                will.dead = True
                engine.add_eff(Ring(will.ipos))

        edge = self.targeting_line.hit_edge((1280, 720))
        engine.add_eff(Beam(engine.mc.ipos, edge, width=self.width))
