import math


def distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dx, dy = x2 - x1, y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)


def direction(pos1, pos2):
    x, y = pos1
    nx, ny = pos2
    dx, dy = float(nx - x), float(ny - y)
    mag = math.sqrt(dx ** 2 + dy ** 2)
    return dx / mag, dy / mag


def shift(pos, towards, dist):
    dir1 = direction(pos, towards)

    x, y = pos
    x += dir1[0] * dist
    y += dir1[1] * dist

    return x, y


def close(pos, target, speed, min_dist, backoff=False):
    d = distance(pos, target)
    if (d-speed) > min_dist:
        return shift(pos, target, speed)
    elif d > min_dist or backoff:
        return shift(pos, target, d - min_dist)
    else:
        return pos


def ipos(pos):
    return map(int, pos)