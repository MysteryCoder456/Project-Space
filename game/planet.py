import math
from glm import vec2, distance
import pygame

from game.entity import Entity


class Planet(Entity):
    def __init__(self, pos: vec2, mass, color):
        """
        Planet Body

        Args:
            pos (vec2): initial position,
            mass (float): mass of body,
            color (tuple/pygame.Color): color of the planet
        """

        super().__init__(pos, mass)
        self.color = color

    def collide(self, entity: Entity):
        dx = self.pos.x - entity.pos.x
        dy = self.pos.y - entity.pos.y
        angle = math.atan2(dy, dx)

        mag = distance(self.pos, self.vel)
        self.vel = vec2(
            math.cos(angle) * mag,
            math.sin(angle) * mag
        )
