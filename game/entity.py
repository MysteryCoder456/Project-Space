import math
import pygame
from glm import vec2, distance


class Entity:
    def __init__(self, pos: vec2, mass):
        """
        Celestial Body

        Args:
            pos (vec2): inital position,
            mass (float/int): mass of body,
        """

        self.pos: vec2 = pos
        self.mass = mass
        self.vel: vec2 = vec2(0)

        self.radius = math.sqrt(mass) * 5
        self.color = (0, 0, 0)

    def attract_towards(self, entity):
        # Get the distance and gravitational force
        r = distance(entity.pos, self.pos)
        G = 6000
        F = (entity.mass * self.mass) / r**2 * G

        # Calculate gravitaional vector
        diff = entity.pos - self.pos
        normalized = diff / distance(entity.pos, self.pos)
        acceleration = (normalized * F) / self.mass # F=ma

        # Add the vector to the velocity
        self.vel += acceleration

    def update(self, dt):
        self.pos += self.vel * dt

    def render(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.radius)
