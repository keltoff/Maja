import ezpygame_fixed as ez
import pygame
import arena
from arena import engine, mc, creep


class Battle(ez.Scene):
    def __init__(self):
        self.engine = engine.Engine.build()
        self.engine.add(creep.Creep(500, 100))
        self.engine.add(creep.Creep(150, 120))
        self.engine.add(creep.Creep(150, 130))
        self.engine.add(creep.Creep(150, 140))

        self.engine.mc = arena.mc.Main(130, 250)

        self.mode = 'turn'

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20, bold=False)

    def draw(self, screen):
        screen.fill((250, 150, 70))

        for c in self.engine.creeps:
            if c.tail:
                pygame.draw.line(screen, (50, 50, 50), c.pos, c.tail, 6)

            pygame.draw.circle(screen, (50, 50, 50), c.ipos, 6)
            pygame.draw.circle(screen, (0, 0, 0), c.ipos, 6, 1)

        if self.engine.mc.tail:
            pygame.draw.line(screen, (0, 0, 100), self.engine.mc.pos, self.engine.mc.tail, 10)

        pygame.draw.circle(screen, (30, 70, 250), self.engine.mc.ipos, 10)
        pygame.draw.circle(screen, (0, 0, 100), self.engine.mc.ipos, 10, 1)

         # HUD
        screen.blit(self.font.render(self.mode, 10, (250, 250, 250)), (30, 30))

    def update(self, dt):
        if self.mode == 'rt':
            self.engine.tick(dt)

        self.engine.update(dt)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if event.button == 1:
                self.engine.add(creep.Creep(x, y))
            if event.button == 3:
                self.engine.mc.target = event.pos
                if self.mode == 'turn':
                    self.engine.turn()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if self.mode == 'rt':
                    self.mode = 'turn'
                else:
                    self.mode = 'rt'

