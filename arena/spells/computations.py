import math


class Line:
    def __init__(self, start, target):
        sx, sy = start
        tx, ty = target

        dx = tx - sx
        dy = ty - sy
        l = math.sqrt(dx ** 2 + dy ** 2)

        self.nx = dx / l
        self.ny = dy / l

        self.c_lateral = self.ny * sx - self.nx * sy
        self.c_longitudinal = self.nx * sx + self.ny * sy

    def get_distance(self, (tx, ty)):
        longitudinal = self.nx * tx + self.ny * ty - self.c_longitudinal
        lateral = abs(self.ny * tx - self.nx * ty - self.c_lateral)
        return longitudinal, lateral

    def hit_edge(self, (w, h)):
        if self.nx > 0:
            return w, int((self.ny * w - self.c_lateral) / self.nx)
        else:
            return 0, int(- self.c_lateral / self.nx)


class Arc:
    def __init__(self, start, target):
        self.sx, self.sy = start

        tx, ty = target
        self.angle = math.degrees(math.atan2(ty - self.sy, tx - self.sx))

    def get_polar(self, (tx, ty)):
        dx = tx - self.sx
        dy = ty - self.sy
        distance = math.sqrt(dx ** 2 + dy ** 2)
        angle_r = math.atan2(dy, dx)
        angle = math.degrees(angle_r) - self.angle
        if angle < -180:
            angle += 360
        if angle > 180:
            angle -= 360
        return distance, abs(angle)