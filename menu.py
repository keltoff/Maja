import ezpygame_fixed as ez
import pygame


class Menu(ez.Scene):
    def __init__(self):
        pass


    def __init__(self):
        pass
        # self.font = pygame.font.Font('arial', 10)

    def on_enter(self, previous_scene):
        self.application.title = 'Main Menu'
        self.application.resolution = (640, 480)
        self.application.update_rate = 30

    def draw(self, screen):
        pass
        # pygame.draw.rect(...)
        # text = self.font.render(...)
        # screen.blit(text, ...)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                game_size = self._get_game_size(event.pos)
                # self.change_scene(Game(game_size))

    def _get_game_size(self, mouse_pos_upon_click):
        pass

    def update(self, dt):
        pass

