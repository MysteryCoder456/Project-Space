import pygame
import math
from uni_vars import win


class Planet:
    def __init__(self, pos, direc, speed, radius, color):
        self.x = pos[0]
        self.y = pos[1]
        self.direction = direc
        self.speed = speed
        self.x_vel = math.cos(self.direction) * self.speed
        self.y_vel = math.sin(self.direction) * self.speed
        self.radius = radius
        self.mass = self.radius * 1.2
        self.color = color
        self.draw_x = self.x - self.radius
        self.draw_y = self.y - self.radius

    def set_dir(self, angle):
        self.direction = angle

    def apply_friction(self, friction):
        self.x_vel *= friction
        self.y_vel *= friction

    def render(self):
        pygame.draw.ellipse(win, self.color, (self.draw_x, self.draw_y, self.radius * 2, self.radius * 2))

    def update(self):
        dx = self.x - self.x_vel
        dy = self.y - self.y_vel
        angle = math.atan2(dy, dx)
        self.set_dir(angle)

        mass_div = 25

        self.x += self.x_vel / (self.mass / mass_div)
        self.y += self.y_vel / (self.mass / mass_div)
        self.draw_x = self.x - self.radius
        self.draw_y = self.y - self.radius
