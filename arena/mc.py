import pos_math as pmath
from ent import Entity
import pygame


class Main(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)

        self.target = None
        self.speed = 0.5

    def ticks(self, dt):
        self.move(dt)


    def move(self, dist):
        if self.target:

            self.tail = self.pos
            self.tail_duration = 500

            self.pos = pmath.close(self.pos, self.target, dist*self.speed, 0)
            if pmath.distance(self.pos, self.target) < self.speed:
                self.target = None

    def draw(self, screen):
        if self.tail:
            pygame.draw.line(screen, (0, 0, 100), self.pos, self.tail, 10)

        pygame.draw.circle(screen, (30, 70, 250), self.ipos, 10)
        pygame.draw.circle(screen, (0, 0, 100), self.ipos, 10, 1)