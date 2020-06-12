from glm import vec2
import pygame

from game.entity import Entity


class Planet(Entity):
    def __init__(self, pos: vec2, mass, color):
        """
        Planet Body

        Args:
            pos (vec2): initial position,
            mass (float/int): mass of body,
            color (tuple/pygame.Color): color of the planet
        """

        super().__init__(pos, mass)
        self.color = color
