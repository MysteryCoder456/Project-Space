import pygame
import math

width, height = 1200, 750
title = 'Space'
background = (255, 255, 255)
FPS = 60
friction = 0.99

win = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)


def resolve_collision_circle(c1, c2):
    div = 80
    d = dist(c1.x, c1.y, c2.x, c2.y)
    if d < c1.radius + c2.radius:
        speed_x1 = (c1.x - c1.x_vel) / div
        speed_y1 = (c1.y - c1.y_vel) / div
        speed_x2 = (c2.x - c2.x_vel) / div
        speed_y2 = (c2.y - c2.y_vel) / div

        # change c1's direction
        dx = c1.x - c2.x
        dy = c1.y - c2.y
        new_angle = math.atan2(dy, dx) + c1.direction
        c1.x_vel = math.cos(new_angle) * speed_x1
        c1.y_vel = math.sin(new_angle) * speed_y1

        # change c2's direction
        dx = c2.x - c1.x
        dy = c2.y - c1.y
        new_angle = math.atan2(dy, dx) + c2.direction
        c2.x_vel = math.cos(new_angle) * speed_x2
        c2.y_vel = math.sin(new_angle) * speed_y2


def dist(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    c = math.sqrt((a ** 2) + (b ** 2))
    # print(a, b, c)
    return c


def gravity(body1, body2, repel=False):
    dx = body1.x - body2.x
    dy = body1.y - body2.y
    d = dist(body1.x, body1.y, body2.x, body2.y)
    mult = 0.005
    m = body1.mass * body2.mass
    Fx = (dx / (d * d) * m) * mult
    Fy = (dy / (d * d) * m) * mult

    if not repel:
        body2.x_vel += Fx
        body2.y_vel += Fy
        body1.x_vel -= Fx
        body1.y_vel -= Fy
    elif repel:
        body2.x_vel -= Fx
        body2.y_vel -= Fy
        body1.x_vel += Fx
        body1.y_vel += Fy

# def gravity(b1, b2, repel=False):
#     pass
