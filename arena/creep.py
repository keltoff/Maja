import pos_math as pmath
from ent import Entity
import pygame


class Creep(Entity):
    def __init__(self, x=0, y=0):
        Entity.__init__(self, x, y)
        self.dead = False

    def ticks(self, dt):
        self.move(dt)

    def move(self, dist):
        target = self.eng.mc.pos

        self.tail = self.pos
        self.tail_duration = 500

        self.pos = pmath.close(self.pos, target, 0.2 * dist, 100)

    def draw(self, screen):
        if self.tail:
            pygame.draw.line(screen, (50, 50, 50), self.pos, self.tail, 6)

        pygame.draw.circle(screen, (50, 50, 50), self.ipos, 6)
        pygame.draw.circle(screen, (0, 0, 0), self.ipos, 6, 1)

    def alive(self):
        return not self.dead
