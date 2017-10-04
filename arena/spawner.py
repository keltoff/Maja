from ent import Entity
import pos_math as pmath
import pygame
import random
import creep


class Spawner(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)

        self.size = 100

        self.spawn_count = 5
        self.spawn_turns = 4

        self.spawn_remains = self.spawn_turns

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20, bold=False)

    def turn(self):
        self.spawn_remains -= 1

        if self.spawn_remains == 0:
            self.spawn_remains = self.spawn_turns

            # spawn
            for i in range(self.spawn_count):
                # x, y = self.ipos + cis(i, self.spawn.count)*self.size
                x = self.ipos[0] + int((random.random()-0.5) * self.size * 2)
                y = self.ipos[1] + int((random.random()-0.5) * self.size * 2)

                c = creep.Creep(x, y)
                self.eng.add(c)

    def draw(self, screen):
        pygame.draw.circle(screen, (250, 250, 250), self.ipos, self.size)
        pygame.draw.circle(screen, (0, 0, 0), self.ipos, self.size, 1)

        screen.blit(self.font.render(str(self.spawn_remains), 30, (0, 0, 0)), self.ipos)