import computations as cmp
import pygame.draw as pd
import pygame
from pygame.color import Color
from arena.effect import CircularWave, Ring
import math
import sys


class Wave:
    def __init__(self, length=100, arc=60):
        self.targeting_arc = None
        self.arc = arc
        self.length = length
        self.name = 'Wave'

    def targeting(self, origin, cursor):
        self.targeting_arc = cmp.Arc(origin, cursor)

    def draw_cursor(self, canvas, origin, target):
        tx, ty = target
        size = 5
        color = Color('blue')
        pd.line(canvas, color, (tx - size, ty), (tx + size, ty))
        pd.line(canvas, color, (tx, ty - size), (tx, ty + size))

        ox, oy = origin.pos
        t_angle = math.degrees(math.atan2(oy - ty, tx - ox))
        d = self.length
        color = Color('cyan')
        rect = pygame.Rect(ox - d, oy - d, 2 * d, 2 * d)
        pd.arc(canvas, color, rect, math.radians(t_angle - self.arc), math.radians(t_angle + self.arc))

    def targets(self, target_candidate):
        dd, ad = self.targeting_arc.get_polar(target_candidate.pos)
        return 0 <= dd <= self.length and ad <= self.arc

    def draw_aimmark(self, canvas, origin, target):
        tx, ty = target.pos
        ox, oy = origin.pos
        d = int(math.sqrt((ox - tx) ** 2 + (oy - ty) ** 2))

        angle_width = 5

        length_step = 5

        t_angle = math.degrees(math.atan2(oy - ty, tx - ox))

        color = Color('cyan')
        rect = pygame.Rect(ox - d, oy - d, 2 * d, 2 * d)
        pd.arc(canvas, color, rect, math.radians(t_angle - angle_width), math.radians(t_angle + angle_width))
        pd.arc(canvas, color, rect.inflate(length_step, length_step), math.radians(t_angle - angle_width), math.radians(t_angle + angle_width))
        pd.arc(canvas, color, rect.inflate(-length_step, -length_step), math.radians(t_angle - angle_width), math.radians(t_angle + angle_width))


    def proc(self, engine, target):
        self.targeting(engine.mc.pos, target)

        for will in engine.creeps:
            if self.targets(will):
                will.dead = True
                engine.add_eff(Ring(will.ipos))

        tx, ty = target
        ox, oy = engine.mc.ipos
        angle = math.degrees(math.atan2(oy - ty, tx - ox))
        engine.add_eff(CircularWave(engine.mc.ipos, self.length, angle, self.arc))

