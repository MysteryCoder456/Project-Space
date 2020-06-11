import math
import pygame
from glm import vec2, distance


class Entity:
    def __init__(self, pos: vec2, mass):
        self.pos: vec2 = pos
        self.mass = mass
        self.vel: vec2 = vec2(0)

        self.radius = (mass ** 0.5) * 5
        self.color = (0, 0, 0)

    def attract_towards(self, entity):
        # Get the distance and gravitational force
        r = distance(entity.pos, self.pos)
        G = 5
        F = (entity.mass * self.mass) / r**2 * G

        # Calculate gravitaional vector
        diff = entity.pos - self.pos
        angle = math.atan2(diff.y, diff.x)
        acceleration = (vec2(math.cos(angle), math.sin(angle)) * F) / self.mass # F=ma

        # Add the vector to the velocity
        self.vel += acceleration

    def update(self, dt):
        self.pos += self.vel * dt

    def render(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.radius)