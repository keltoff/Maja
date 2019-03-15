

class Spell:
    def __init__(self):
        pass

    def state_text(self):
        pass

    def draw_cursor(self, canvas, origin, target):
        pass

    def draw_aimmark(self, canvas, origin, target):
        pass

    def find_targets(self, origin, cursor_pos, potentials):
        pass

    def targets(self, target_candidate):
        return False