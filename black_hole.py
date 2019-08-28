import pygame
from uni_vars import win, dist
import math


class BlackHole:
    def __init__(self, pos, direc, speed, radius, repulsive=False, static=True):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direc
        self.speed = speed
        self.x_vel = math.cos(self.direction) * self.speed
        self.y_vel = math.sin(self.direction) * self.speed
        self.radius = radius
        self.mass = self.radius * 15
        self.imso = self.radius * 5
        self.draw_x = self.x - self.radius
        self.draw_y = self.y - self.radius
        self.repulsive = repulsive
        self.static = static

    def set_dir(self, angle):
        self.direction = angle

    def collision(self, body):
        d = dist(self.x, self.y, body.x, body.y)

        if d < self.radius + body.radius:
            return True
        else:
            return False

    def render(self):
        pygame.draw.ellipse(win, (0, 0, 0), (self.draw_x, self.draw_y, self.radius * 2, self.radius * 2))
        pygame.draw.arc(win, (200, 200, 200), (self.x - self.imso, self.y - self.imso, self.imso * 2, self.imso * 2),
                        -0.2, 2 * math.pi )

    def update(self):
        dx = self.x - self.x_vel
        dy = self.y - self.y_vel
        angle = math.atan2(dy, dx)
        self.set_dir(angle)

        if not self.static:
            self.x += self.x_vel
            self.y += self.y_vel

        self.draw_x = self.x - self.radius
        self.draw_y = self.y - self.radius
