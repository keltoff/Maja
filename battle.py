import ezpygame_fixed as ez
import pygame
import arena
from arena import engine, mc, creep, spawner


class Battle(ez.Scene):
    def __init__(self):
        self.engine = engine.Engine.build()
        self.engine.add(creep.Creep(500, 100))
        self.engine.add(creep.Creep(150, 120))
        self.engine.add(creep.Creep(150, 130))
        self.engine.add(creep.Creep(150, 140))

        self.engine.mc = arena.mc.Main(130, 250)

        self.engine.add_spawn(spawner.Spawner(200, 200))
        self.engine.add_spawn(spawner.Spawner(500, 500))
        self.engine.add_spawn(spawner.Spawner(800, 200))

        self.mode = 'turn'

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20, bold=False)

    def draw(self, screen):
        screen.fill((250, 150, 70))

        for s in self.engine.spawners:
            s.draw(screen)

        for c in self.engine.creeps:
            c.draw(screen)

        self.engine.mc.draw(screen)

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

